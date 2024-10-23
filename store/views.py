from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.

def home(request):
    return render(request, 'store/home.html')

def product_detail(request, sku):
    product = get_object_or_404(Product, sku)
    return render(request, 'store/product_detail.html', {'product': product})

def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(sku__in=cart.keys())
    return render(request, 'store/cart.html', {'products': products, 'cart': cart})

def add_to_cart(request, sku):
    cart = request.session.get('cart', {})
    cart[sku] = cart.get(sku, 0) + 1
    request.session['cart'] = cart
    return redirect('cart')


def remove_from_cart(request, sku):
    cart = request.session.get('cart', {})
    if sku in cart:
        cart[sku] -= 1
        if cart[sku] <= 0:
            del cart[sku]
    request.session['cart'] = cart
    return redirect('cart')


def delete_from_cart(request, sku):
    cart = request.session.get('cart', {})
    if sku in cart:
        del cart[sku]
    request.session['cart'] = cart
    return redirect('cart')
