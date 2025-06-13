from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Order, ActionLog
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def log_action(action_type, order_id, performed_by="System", details=None):
    """Helper function to log actions"""
    log = ActionLog(
        action_type=action_type,
        performed_by=performed_by,
        order_id=order_id,
        details=details
    )
    db.session.add(log)
    db.session.commit()

@app.route('/')
def index():
    """Display all orders"""
    orders = Order.query.all()
    return render_template('index.html', orders=orders)

@app.route('/add_order', methods=['GET', 'POST'])
def add_order():
    """Add new order"""
    if request.method == 'POST':
        # Generate unique order ID
        order_id = f"ORD-{str(uuid.uuid4())[:8].upper()}"
        
        # Get form data
        num_items = int(request.form['num_items'])
        delivery_date = datetime.strptime(request.form['delivery_date'], '%Y-%m-%d').date()
        sender_name = request.form['sender_name']
        recipient_name = request.form['recipient_name']
        recipient_address = request.form['recipient_address']
        
        # Create new order
        order = Order(
            order_id=order_id,
            num_items=num_items,
            delivery_date=delivery_date,
            sender_name=sender_name,
            recipient_name=recipient_name,
            recipient_address=recipient_address
        )
        
        db.session.add(order)
        db.session.commit()
        
        # Log the action
        log_action("Created", order_id, "User", f"Order created with {num_items} items")
        
        flash(f'Order {order_id} created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_order.html')

@app.route('/edit_order/<order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    """Edit existing order"""
    order = Order.query.filter_by(order_id=order_id).first_or_404()
    
    if request.method == 'POST':
        # Store old values for logging
        old_values = order.to_dict()
        
        # Update order
        order.num_items = int(request.form['num_items'])
        order.delivery_date = datetime.strptime(request.form['delivery_date'], '%Y-%m-%d').date()
        order.sender_name = request.form['sender_name']
        order.recipient_name = request.form['recipient_name']
        order.recipient_address = request.form['recipient_address']
        
        db.session.commit()
        
        # Log the action
        log_action("Edited", order_id, "User", "Order details updated")
        
        flash(f'Order {order_id} updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_order.html', order=order)

@app.route('/mark_delivered/<order_id>')
def mark_delivered(order_id):
    """Mark order as delivered"""
    order = Order.query.filter_by(order_id=order_id).first_or_404()
    
    if order.status != 'Delivered':
        order.status = 'Delivered'
        db.session.commit()
        
        # Log the action
        log_action("Marked Delivered", order_id, "User", "Order status changed to Delivered")
        
        flash(f'Order {order_id} marked as delivered!', 'success')
    else:
        flash(f'Order {order_id} is already delivered!', 'info')
    
    return redirect(url_for('index'))

@app.route('/delete_order/<order_id>')
def delete_order(order_id):
    """Delete order"""
    order = Order.query.filter_by(order_id=order_id).first_or_404()
    
    db.session.delete(order)
    db.session.commit()
    
    # Log the action
    log_action("Deleted", order_id, "User", "Order removed from system")
    
    flash(f'Order {order_id} deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/logs')
def logs():
    """Display action logs"""
    logs = ActionLog.query.order_by(ActionLog.timestamp.desc()).all()
    return render_template('logs.html', logs=logs)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
