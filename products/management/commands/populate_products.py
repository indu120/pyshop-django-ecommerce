from django.core.management.base import BaseCommand
from django.utils import timezone
from products.models import Category, Product, Offer
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Populate the database with sample products and categories'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate database...'))
        
        # Create categories
        categories_data = [
            {
                'name': 'Electronics',
                'description': 'Latest electronic gadgets and devices',
            },
            {
                'name': 'Clothing',
                'description': 'Trendy fashion and apparel for all ages',
            },
            {
                'name': 'Home & Kitchen',
                'description': 'Everything you need for your home and kitchen',
            },
            {
                'name': 'Books',
                'description': 'Wide collection of books across all genres',
            },
            {
                'name': 'Sports & Outdoors',
                'description': 'Sports equipment and outdoor gear',
            },
            {
                'name': 'Beauty & Personal Care',
                'description': 'Beauty products and personal care items',
            },
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'description': cat_data['description'],
                }
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Sample products data
        products_data = [
            # Electronics
            {
                'name': 'Smartphone Pro Max 256GB',
                'category': 'Electronics',
                'description': 'Latest flagship smartphone with advanced camera system, powerful processor, and long-lasting battery. Features include 5G connectivity, wireless charging, and premium build quality.',
                'short_description': 'Premium smartphone with advanced features and excellent performance.',
                'price': Decimal('999.99'),
                'old_price': Decimal('1199.99'),
                'stock': 50,
                'featured': True,
                'rating': Decimal('4.8'),
                'image_url': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=400&fit=crop',
            },
            {
                'name': 'Wireless Bluetooth Headphones',
                'category': 'Electronics',
                'description': 'Premium wireless headphones with active noise cancellation, superior sound quality, and comfortable design. Perfect for music lovers and professionals.',
                'short_description': 'High-quality wireless headphones with noise cancellation.',
                'price': Decimal('199.99'),
                'old_price': Decimal('249.99'),
                'stock': 75,
                'featured': True,
                'rating': Decimal('4.6'),
                'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=400&fit=crop',
            },
            {
                'name': '4K Smart TV 55 inch',
                'category': 'Electronics',
                'description': 'Ultra HD 4K Smart TV with HDR support, built-in streaming apps, and voice control. Enjoy cinema-quality entertainment at home.',
                'short_description': 'Large 4K Smart TV with premium features and streaming capabilities.',
                'price': Decimal('799.99'),
                'stock': 25,
                'featured': False,
                'rating': Decimal('4.5'),
                'image_url': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400&h=400&fit=crop',
            },
            {
                'name': 'Gaming Laptop RTX 4070',
                'category': 'Electronics',
                'description': 'High-performance gaming laptop with RTX 4070 graphics, Intel i7 processor, 16GB RAM, and 1TB SSD. Perfect for gaming and creative work.',
                'short_description': 'Powerful gaming laptop with RTX graphics and high-end specs.',
                'price': Decimal('1499.99'),
                'stock': 15,
                'featured': True,
                'rating': Decimal('4.7'),
                'image_url': 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400&h=400&fit=crop',
            },
            
            # Clothing
            {
                'name': 'Premium Cotton T-Shirt',
                'category': 'Clothing',
                'description': 'Comfortable premium cotton t-shirt with modern fit. Available in multiple colors and sizes. Perfect for casual wear and everyday comfort.',
                'short_description': 'Soft and comfortable premium cotton t-shirt.',
                'price': Decimal('29.99'),
                'old_price': Decimal('39.99'),
                'stock': 100,
                'featured': False,
                'rating': Decimal('4.3'),
                'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=400&fit=crop',
            },
            {
                'name': 'Denim Jacket Classic Blue',
                'category': 'Clothing',
                'description': 'Classic blue denim jacket made from premium denim fabric. Timeless style that goes with everything. Durable construction and comfortable fit.',
                'short_description': 'Stylish classic blue denim jacket for all occasions.',
                'price': Decimal('89.99'),
                'stock': 60,
                'featured': False,
                'rating': Decimal('4.4'),
                'image_url': 'https://images.unsplash.com/photo-1544966503-7cc5ac882d2c?w=400&h=400&fit=crop',
            },
            {
                'name': 'Designer Sneakers White',
                'category': 'Clothing',
                'description': 'Premium designer sneakers with leather upper, comfortable cushioning, and modern design. Perfect for casual and semi-formal occasions.',
                'short_description': 'Stylish white designer sneakers with premium materials.',
                'price': Decimal('159.99'),
                'old_price': Decimal('199.99'),
                'stock': 40,
                'featured': True,
                'rating': Decimal('4.6'),
                'image_url': 'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400&h=400&fit=crop',
            },
            {
                'name': 'Elegant Dress Black',
                'category': 'Clothing',
                'description': 'Elegant black dress perfect for formal occasions and evening events. Made from high-quality fabric with sophisticated design and comfortable fit.',
                'short_description': 'Sophisticated black dress for formal occasions.',
                'price': Decimal('129.99'),
                'stock': 30,
                'featured': False,
                'rating': Decimal('4.5'),
                'image_url': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400&h=400&fit=crop',
            },
            
            # Home & Kitchen
            {
                'name': 'Professional Chef Knife Set',
                'category': 'Home & Kitchen',
                'description': 'Professional-grade chef knife set with high-carbon stainless steel blades. Includes essential knives for all cooking needs with wooden storage block.',
                'short_description': 'Complete professional chef knife set with storage block.',
                'price': Decimal('199.99'),
                'old_price': Decimal('259.99'),
                'stock': 35,
                'featured': True,
                'rating': Decimal('4.8'),
                'image_url': 'https://images.unsplash.com/photo-1593618998160-e34014e67546?w=400&h=400&fit=crop',
            },
            {
                'name': 'Luxury Bedding Set Queen',
                'category': 'Home & Kitchen',
                'description': 'Luxury bedding set made from premium Egyptian cotton. Includes fitted sheet, flat sheet, and pillowcases. Soft, breathable, and durable.',
                'short_description': 'Premium Egyptian cotton bedding set for ultimate comfort.',
                'price': Decimal('149.99'),
                'stock': 45,
                'featured': False,
                'rating': Decimal('4.7'),
                'image_url': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=400&h=400&fit=crop',
            },
            {
                'name': 'Smart Coffee Maker',
                'category': 'Home & Kitchen',
                'description': 'Smart coffee maker with programmable settings, built-in grinder, and smartphone connectivity. Brew perfect coffee with customizable strength and temperature.',
                'short_description': 'Smart programmable coffee maker with built-in grinder.',
                'price': Decimal('299.99'),
                'stock': 20,
                'featured': False,
                'rating': Decimal('4.4'),
                'image_url': 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=400&h=400&fit=crop',
            },
            
            # Books
            {
                'name': 'The Art of Programming',
                'category': 'Books',
                'description': 'Comprehensive guide to modern programming practices and software development. Covers algorithms, data structures, and best practices for professional developers.',
                'short_description': 'Essential programming book for developers and students.',
                'price': Decimal('49.99'),
                'old_price': Decimal('59.99'),
                'stock': 80,
                'featured': False,
                'rating': Decimal('4.6'),
                'image_url': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&h=400&fit=crop',
            },
            {
                'name': 'Mystery Novel: The Lost Key',
                'category': 'Books',
                'description': 'Thrilling mystery novel about a detective solving an ancient puzzle. Full of twists, turns, and unexpected revelations that will keep you reading all night.',
                'short_description': 'Captivating mystery novel with unexpected twists.',
                'price': Decimal('14.99'),
                'stock': 120,
                'featured': False,
                'rating': Decimal('4.2'),
                'image_url': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=400&h=400&fit=crop',
            },
            {
                'name': 'Cookbook: Healthy Meals',
                'category': 'Books',
                'description': 'Collection of delicious and healthy recipes for every meal. Includes nutritional information, cooking tips, and beautiful food photography.',
                'short_description': 'Comprehensive cookbook with healthy and delicious recipes.',
                'price': Decimal('24.99'),
                'stock': 65,
                'featured': False,
                'rating': Decimal('4.5'),
                'image_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop',
            },
            
            # Sports & Outdoors
            {
                'name': 'Professional Yoga Mat',
                'category': 'Sports & Outdoors',
                'description': 'High-quality yoga mat with superior grip and cushioning. Made from eco-friendly materials, perfect for all yoga styles and fitness routines.',
                'short_description': 'Premium eco-friendly yoga mat with excellent grip.',
                'price': Decimal('79.99'),
                'old_price': Decimal('99.99'),
                'stock': 55,
                'featured': True,
                'rating': Decimal('4.7'),
                'image_url': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400&h=400&fit=crop',
            },
            {
                'name': 'Camping Tent 4-Person',
                'category': 'Sports & Outdoors',
                'description': 'Waterproof 4-person camping tent with easy setup and durable construction. Perfect for family camping trips and outdoor adventures.',
                'short_description': 'Spacious waterproof camping tent for outdoor adventures.',
                'price': Decimal('189.99'),
                'stock': 25,
                'featured': False,
                'rating': Decimal('4.3'),
                'image_url': 'https://images.unsplash.com/photo-1504851149312-7a075b496cc7?w=400&h=400&fit=crop',
            },
            {
                'name': 'Adjustable Dumbbells Set',
                'category': 'Sports & Outdoors',
                'description': 'Adjustable dumbbell set with quick-change weight system. Perfect for home gym workouts with space-saving design and durable construction.',
                'short_description': 'Space-saving adjustable dumbbells for home workouts.',
                'price': Decimal('299.99'),
                'stock': 20,
                'featured': False,
                'rating': Decimal('4.6'),
                'image_url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&h=400&fit=crop',
            },
            
            # Beauty & Personal Care
            {
                'name': 'Luxury Skincare Set',
                'category': 'Beauty & Personal Care',
                'description': 'Complete luxury skincare set with cleanser, toner, serum, and moisturizer. Made with natural ingredients for all skin types.',
                'short_description': 'Premium skincare set with natural ingredients.',
                'price': Decimal('159.99'),
                'old_price': Decimal('199.99'),
                'stock': 40,
                'featured': True,
                'rating': Decimal('4.8'),
                'image_url': 'https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400&h=400&fit=crop',
            },
            {
                'name': 'Professional Hair Dryer',
                'category': 'Beauty & Personal Care',
                'description': 'Professional-grade hair dryer with ionic technology and multiple heat settings. Fast drying with reduced frizz and enhanced shine.',
                'short_description': 'Professional ionic hair dryer for salon-quality results.',
                'price': Decimal('129.99'),
                'stock': 30,
                'featured': False,
                'rating': Decimal('4.4'),
                'image_url': 'https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=400&h=400&fit=crop',
            },
            {
                'name': 'Organic Face Masks Set',
                'category': 'Beauty & Personal Care',
                'description': 'Set of organic face masks for different skin concerns. Includes hydrating, purifying, and anti-aging masks made with natural ingredients.',
                'short_description': 'Organic face mask set for various skin care needs.',
                'price': Decimal('49.99'),
                'stock': 70,
                'featured': False,
                'rating': Decimal('4.3'),
                'image_url': 'https://images.unsplash.com/photo-1570194065650-d99fb4bedf7a?w=400&h=400&fit=crop',
            },
        ]
        
        # Create products
        for product_data in products_data:
            category = categories[product_data['category']]
            
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'category': category,
                    'description': product_data['description'],
                    'short_description': product_data['short_description'],
                    'price': product_data['price'],
                    'old_price': product_data.get('old_price'),
                    'stock': product_data['stock'],
                    'featured': product_data['featured'],
                    'rating': product_data['rating'],
                    'image_url': product_data['image_url'],
                    'is_active': True,
                }
            )
            
            if created:
                self.stdout.write(f'Created product: {product.name}')
        
        # Create sample offers
        offers_data = [
            {
                'code': 'WELCOME10',
                'name': 'Welcome Discount',
                'description': '10% off for new customers',
                'discount_type': 'percentage',
                'discount': Decimal('10.00'),
                'minimum_amount': Decimal('50.00'),
                'usage_limit': 100,
                'valid_from': timezone.now(),
                'valid_to': timezone.now() + timezone.timedelta(days=30),
            },
            {
                'code': 'SUMMER20',
                'name': 'Summer Sale',
                'description': '20% off summer collection',
                'discount_type': 'percentage',
                'discount': Decimal('20.00'),
                'minimum_amount': Decimal('100.00'),
                'usage_limit': 50,
                'valid_from': timezone.now(),
                'valid_to': timezone.now() + timezone.timedelta(days=60),
            },
            {
                'code': 'SAVE50',
                'name': 'Fixed Discount',
                'description': '$50 off orders over $200',
                'discount_type': 'fixed',
                'discount': Decimal('50.00'),
                'minimum_amount': Decimal('200.00'),
                'usage_limit': 25,
                'valid_from': timezone.now(),
                'valid_to': timezone.now() + timezone.timedelta(days=45),
            },
        ]
        
        for offer_data in offers_data:
            offer, created = Offer.objects.get_or_create(
                code=offer_data['code'],
                defaults=offer_data
            )
            
            if created:
                self.stdout.write(f'Created offer: {offer.code} - {offer.name}')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully populated database with:\n'
                f'- {Category.objects.count()} categories\n'
                f'- {Product.objects.count()} products\n'
                f'- {Offer.objects.count()} offers\n'
            )
        )
        
        self.stdout.write(
            self.style.WARNING(
                '\nYou can now:\n'
                '1. Visit http://127.0.0.1:8000/ to see your ecommerce site\n'
                '2. Visit http://127.0.0.1:8000/admin/ to manage products\n'
                '3. Login with your superuser account to access admin features\n'
            )
        )
