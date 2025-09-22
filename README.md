# PyShop - Modern Django Ecommerce

A full-featured, modern ecommerce web application built with Django, Bootstrap, and modern web technologies. PyShop provides a complete online shopping experience with user authentication, product management, shopping cart functionality, and an intuitive admin interface.

## 🌟 Features

### Customer Features
- **Modern UI/UX**: Responsive design built with Bootstrap 5 and custom CSS
- **Product Catalog**: Browse products by category with advanced filtering and search
- **Product Details**: Detailed product pages with images, descriptions, and customer reviews
- **Shopping Cart**: Add/remove products, update quantities with session-based cart
- **User Authentication**: Register, login, and manage user accounts
- **Product Reviews**: Rate and review products (authenticated users)
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices

### Admin Features
- **Enhanced Admin Interface**: Custom Django admin with improved product management
- **Category Management**: Organize products into categories with slugs
- **Product Management**: Comprehensive product CRUD with image handling
- **Order Management**: View and manage customer carts and orders
- **Review Moderation**: Manage customer reviews and ratings
- **Offer Management**: Create and manage discount codes and promotions

### Technical Features
- **Modern Django**: Built with Django 4.2+ following best practices
- **Image Handling**: Upload and manage product images with Pillow
- **SEO Friendly**: Clean URLs with slugs and proper meta tags
- **Security**: CSRF protection, secure authentication, and input validation
- **Database**: SQLite for development, easily configurable for production databases
- **Static Files**: Organized static file structure with WhiteNoise support

## 🛠️ Technology Stack

- **Backend**: Django 4.2+
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **UI Framework**: Bootstrap 5
- **Database**: SQLite (development), PostgreSQL/MySQL (production)
- **Image Processing**: Pillow
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Inter)

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/pyshop-ecommerce.git
   cd pyshop-ecommerce
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
pyshop/
├── pyshop/                 # Main project directory
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── products/              # Products app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # App URL configuration
│   ├── admin.py           # Admin configuration
│   ├── forms.py           # Django forms
│   └── templates/         # HTML templates
├── static/                # Static files
│   ├── css/              # Custom CSS
│   ├── js/               # Custom JavaScript
│   └── images/           # Static images
├── media/                 # User-uploaded files
├── requirements.txt       # Python dependencies
└── manage.py             # Django management script
```

## 🎯 Usage

### For Customers
1. **Browse Products**: Visit the homepage to see featured products and categories
2. **Search**: Use the search bar to find specific products
3. **Product Details**: Click on any product to view detailed information
4. **Add to Cart**: Select quantity and add products to your shopping cart
5. **Register/Login**: Create an account to leave reviews and track orders
6. **Review Products**: Rate and review products you've purchased

### For Administrators
1. **Access Admin**: Go to `/admin/` and login with superuser credentials
2. **Manage Categories**: Create and organize product categories
3. **Add Products**: Add new products with images, descriptions, and pricing
4. **Monitor Orders**: View customer carts and order information
5. **Manage Reviews**: Moderate customer reviews and ratings
6. **Create Offers**: Set up discount codes and promotional offers

## 🚀 Deployment

### Heroku Deployment

1. **Install Heroku CLI** and login
2. **Create requirements.txt** (already included)
3. **Create Procfile**:
   ```
   web: gunicorn pyshop.wsgi
   ```
4. **Update settings.py** for production:
   ```python
   import os
   DEBUG = False
   ALLOWED_HOSTS = ['your-app.herokuapp.com']
   ```
5. **Deploy**:
   ```bash
   heroku create your-app-name
   git add .
   git commit -m "Initial commit"
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### Traditional Server Deployment

1. **Install dependencies** on your server
2. **Configure database** (PostgreSQL/MySQL recommended)
3. **Set up static file serving** with WhiteNoise or nginx
4. **Configure environment variables**
5. **Run migrations** and collect static files
6. **Set up WSGI server** (Gunicorn recommended)

## 🔧 Configuration

### Environment Variables
Create a `.env` file for sensitive settings:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### Database Configuration
For PostgreSQL production setup:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pyshop_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and commit: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Write descriptive commit messages
- Add tests for new features
- Update documentation as needed
- Ensure responsive design compatibility

## 🐛 Bug Reports & Feature Requests

Please use the [GitHub Issues](https://github.com/yourusername/pyshop-ecommerce/issues) page to report bugs or request features.

When reporting bugs, please include:
- Python version
- Django version
- Browser and version
- Steps to reproduce
- Expected vs actual behavior

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **INDULEKHA** - *Initial work* - [GitHub](https://github.com/indu120)

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the responsive CSS framework
- Font Awesome for the beautiful icons
- All contributors who help improve this project

## 📈 Roadmap

### Upcoming Features
- [ ] Payment gateway integration (Stripe, PayPal)
- [ ] Email notifications for orders
- [ ] Wishlist functionality
- [ ] Advanced product filters
- [ ] Multi-language support
- [ ] Social media authentication
- [ ] Product comparison feature
- [ ] Inventory management system
- [ ] Sales analytics dashboard
- [ ] Mobile app (React Native)

### Performance Improvements
- [ ] Database query optimization
- [ ] Image compression and CDN integration
- [ ] Caching implementation (Redis)
- [ ] API development for mobile app

---

**Made with ❤️ using Django and Bootstrap**

For support or questions, please open an issue or contact [indubethur@gmail.com](mailto:indubethur@gmail.com)
