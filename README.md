# 📦 Order Management System

A modern, full-featured **Order Handling System** built with Flask, featuring a beautiful UI with gradient designs, comprehensive order management, and detailed action logging.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.0.5-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🎯 Core Functionality
- **📝 Order Creation** - Add new orders with unique auto-generated IDs
- **✏️ Order Management** - Edit existing orders seamlessly
- **✅ Status Updates** - Mark orders as delivered with one click
- **🗑️ Order Deletion** - Remove orders with confirmation dialogs
- **📊 Action Logging** - Complete audit trail of all system activities
- **📋 Order Display** - Clean, organized view of all orders

### 🎨 Modern UI/UX
- **🌈 Gradient Design** - Beautiful purple-blue gradient backgrounds
- **💎 Glass Morphism** - Semi-transparent containers with backdrop blur
- **🎭 Animated Elements** - Smooth hover effects and transitions
- **📱 Responsive Design** - Optimized for desktop, tablet, and mobile
- **🔤 Poppins Typography** - Modern, professional font throughout
- **🎪 Interactive Components** - Enhanced buttons, forms, and tables

### 🔧 Technical Features
- **🗄️ SQLite Database** - Lightweight, file-based database
- **🏗️ SQLAlchemy ORM** - Robust database operations
- **🔒 Form Validation** - Client and server-side validation
- **📝 Flash Messages** - User feedback for all actions
- **🎨 CSS Grid/Flexbox** - Modern layout techniques
- **⚡ Fast Performance** - Optimized loading and rendering

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/M-Sarim/OrderManagementSystem.git
   cd OrderManagementSystem
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
OrderManagementSystem/
├── 📄 app.py                 # Main Flask application
├── 📄 models.py              # Database models (Order, ActionLog)
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # Project documentation
├── 📁 templates/            # HTML templates
│   ├── 📄 base.html         # Base template with enhanced styling
│   ├── 📄 index.html        # Orders listing page
│   ├── 📄 add_order.html    # Add order form
│   ├── 📄 edit_order.html   # Edit order form
│   └── 📄 logs.html         # Action logs display
└── 📄 orders.db            # SQLite database (auto-created)
```

## 🎮 Usage Guide

### Adding a New Order
1. Click **"Add Order"** button
2. Fill in the required information:
   - Number of items
   - Delivery date
   - Sender name
   - Recipient name
   - Recipient address
3. Click **"Create Order"** to save

### Managing Orders
- **Edit**: Click the blue "Edit" button to modify order details
- **Mark Delivered**: Click the green "Mark Delivered" button to update status
- **Delete**: Click the red "Delete" button to remove an order (with confirmation)

### Viewing Action Logs
- Navigate to **"Action Logs"** to see complete audit trail
- All actions are timestamped and include details

## 🛠️ API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Display all orders |
| `GET/POST` | `/add_order` | Add new order form/submission |
| `GET/POST` | `/edit_order/<order_id>` | Edit order form/submission |
| `GET` | `/mark_delivered/<order_id>` | Mark order as delivered |
| `GET` | `/delete_order/<order_id>` | Delete order |
| `GET` | `/logs` | View action logs |

## 💾 Database Schema

### Orders Table
```sql
- id (Primary Key)
- order_id (Unique, Auto-generated)
- num_items (Integer)
- delivery_date (Date)
- sender_name (String)
- recipient_name (String)
- recipient_address (Text)
- status (String, Default: 'Ongoing')
- created_at (DateTime)
```

### Action Logs Table
```sql
- id (Primary Key)
- action_type (String)
- performed_by (String)
- timestamp (DateTime)
- order_id (String)
- details (Text)
```

## 🎨 Design System

### Color Palette
- **Primary Blue**: `#007bff` → `#0056b3`
- **Success Green**: `#28a745` → `#20c997`
- **Danger Red**: `#dc3545` → `#c82333`
- **Warning Yellow**: `#fff3cd` → `#ffeaa7`
- **Background Gradient**: `#667eea` → `#764ba2`

### Typography
- **Font Family**: Poppins (Google Fonts)
- **Weights Used**: 300, 400, 500, 600, 700
- **Optimized Loading**: Preconnect and font-display: swap

## 🔧 Customization

### Adding New Fields
1. Update the `Order` model in `models.py`
2. Create database migration or delete `orders.db` for fresh start
3. Update forms in templates
4. Modify routes in `app.py`

### Styling Changes
- All styles are in `templates/base.html`
- Modify CSS variables for quick theme changes
- Responsive breakpoints at 768px

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
1. Set `debug=False` in `app.py`
2. Use a production WSGI server like Gunicorn
3. Configure environment variables
4. Set up proper database (PostgreSQL/MySQL for production)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flask** - Micro web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **Google Fonts** - Poppins typography
- **Modern CSS** - Gradient and animation techniques

## 📞 Support

If you encounter any issues or have questions:
1. Check the existing issues
2. Create a new issue with detailed description
3. Include steps to reproduce the problem

## 📸 Screenshots

### Main Dashboard
![Dashboard](https://via.placeholder.com/800x500/667eea/ffffff?text=Order+Management+Dashboard)

### Add Order Form
![Add Order](https://via.placeholder.com/600x400/28a745/ffffff?text=Add+New+Order+Form)

### Action Logs
![Action Logs](https://via.placeholder.com/800x400/007bff/ffffff?text=Action+Logs+View)

## 🔍 Features in Detail

### Order ID Generation
- **Format**: `ORD-XXXXXXXX` (8 character unique identifier)
- **Algorithm**: UUID4-based generation ensures uniqueness
- **Example**: `ORD-7A1CC701`, `ORD-B2F9E834`

### Status Management
- **Ongoing**: Default status for new orders (Yellow badge)
- **Delivered**: Final status for completed orders (Green badge)
- **Visual Indicators**: Color-coded badges with gradients

### Action Logging System
Comprehensive logging of all system activities:
- ✅ **Created** - New order added to system
- ✏️ **Edited** - Order details modified
- 🚚 **Marked Delivered** - Status changed to delivered
- 🗑️ **Deleted** - Order removed from system

## 🧪 Testing

### Manual Testing Checklist
- [ ] Create new order with all fields
- [ ] Edit existing order
- [ ] Mark order as delivered
- [ ] Delete order with confirmation
- [ ] View action logs
- [ ] Test responsive design on mobile
- [ ] Verify form validation

### Test Data
```python
# Sample order data for testing
{
    "num_items": 5,
    "delivery_date": "2024-12-25",
    "sender_name": "John Doe",
    "recipient_name": "Jane Smith",
    "recipient_address": "123 Main St, City, State 12345"
}
```

## 🔧 Troubleshooting

### Common Issues

**Database not found error**
```bash
# Solution: Run the app to auto-create database
python app.py
```

**Port already in use**
```bash
# Solution: Change port in app.py or kill existing process
app.run(debug=True, port=5001)
```

**Font not loading**
- Check internet connection for Google Fonts
- Fonts will fallback to system fonts if unavailable

### Performance Tips
- Database is automatically created on first run
- SQLite is suitable for development and small deployments
- For production, consider PostgreSQL or MySQL

## 🚀 Future Enhancements

### Planned Features
- [ ] **User Authentication** - Login/logout system
- [ ] **Order Search** - Search and filter orders
- [ ] **Export Functionality** - PDF/CSV export
- [ ] **Email Notifications** - Automated status updates
- [ ] **Dashboard Analytics** - Order statistics and charts
- [ ] **Bulk Operations** - Multiple order management
- [ ] **Order Tracking** - Real-time delivery tracking
- [ ] **API Endpoints** - RESTful API for integrations

### Technical Improvements
- [ ] **Database Migrations** - Alembic integration
- [ ] **Unit Tests** - Comprehensive test suite
- [ ] **Docker Support** - Containerization
- [ ] **CI/CD Pipeline** - Automated testing and deployment
- [ ] **Logging System** - Application logging
- [ ] **Configuration Management** - Environment-based configs

---

**Made with ❤️ using Flask and modern web technologies**

*Order Management System v1.0 - Built for efficiency, designed for beauty*
