import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from store.models import Product

# List of sample products
products = [
    {
        'name': 'Backpack',
        'description': 'Durable travel backpack with multiple compartments.',
        'price': 1599.00,
        'image': 'products/backpack.webp'
    },
    {
        'name': 'Headphones',
        'description': 'Noise-cancelling over-ear headphones.',
        'price': 2299.00,
        'image': 'products/headphones.jpeg'
    },
    {
        'name': 'Smartphone',
        'description': 'Latest Android smartphone with OLED display.',
        'price': 24999.00,
        'image': 'products/smartphone.jpeg'
    },
    {
        'name': 'Smart TV',
        'description': '50-inch 4K Smart TV with HDR support.',
        'price': 37999.00,
        'image': 'products/tv.jpeg'
    },
    {
        'name': 'Wrist Watch',
        'description': 'Elegant wristwatch with leather strap.',
        'price': 1299.00,
        'image': 'products/watch.jpeg'
    },
]

# Add to database
for item in products:
    Product.objects.create(
        name=item['name'],
        description=item['description'],
        price=item['price'],
        image=item['image']
    )

print("✅ Sample products added successfully!")
