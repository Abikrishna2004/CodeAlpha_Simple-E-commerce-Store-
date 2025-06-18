# fix_product_images.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from store.models import Product

product_images = {
    "Backpack": "product_images/backpack.webp",
    "Headphones": "product_images/headphones.jpeg",
    "Smartphone": "product_images/smartphone.jpeg",
    "TV": "product_images/tv.jpeg",
    "Watch": "product_images/watch.jpeg",
}

for name, image_path in product_images.items():
    try:
        matching_products = Product.objects.filter(name=name)
        if matching_products.exists():
            for product in matching_products:
                product.image = image_path
                product.save()
                print(f"✅ Updated image for {product.name}")
        else:
            print(f"❌ Product not found: {name}")
    except Exception as e:
        print(f"❌ Error for {name}: {e}")
