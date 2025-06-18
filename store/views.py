from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('home')
    return render(request, 'store/checkout.html')

    

from django.contrib import messages

def order_placed(request):
    payment_method = request.POST.get('payment_method', 'Not selected')
    request.session['cart'] = {}  # clear cart
    return render(request, 'store/order_placed.html', {'payment_method': payment_method})



def checkout(request):
    return render(request, 'store/checkout.html')


def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 1) + 1
    request.session['cart'] = cart
    return redirect('view_cart')

def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1
        else:
            cart.pop(str(product_id))
    request.session['cart'] = cart
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('view_cart')
