from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(50), unique=True, nullable=False)
    num_items = db.Column(db.Integer, nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    sender_name = db.Column(db.String(100), nullable=False)
    recipient_name = db.Column(db.String(100), nullable=False)
    recipient_address = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Ongoing', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Order {self.order_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'num_items': self.num_items,
            'delivery_date': self.delivery_date.strftime('%Y-%m-%d'),
            'sender_name': self.sender_name,
            'recipient_name': self.recipient_name,
            'recipient_address': self.recipient_address,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class ActionLog(db.Model):
    __tablename__ = 'action_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    action_type = db.Column(db.String(50), nullable=False)
    performed_by = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    order_id = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text)
    
    def __repr__(self):
        return f'<ActionLog {self.action_type} on {self.order_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'action_type': self.action_type,
            'performed_by': self.performed_by,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'order_id': self.order_id,
            'details': self.details
        }
