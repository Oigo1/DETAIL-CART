from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import SignUpForm

# Create your views here.

def home(request):
    products = Product.objects.all() #Fetch all products from the database
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, sku):
    product = get_object_or_404(Product, sku=sku)
    images = product.images.all() # Fetch related images
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

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'store/signup.html', {'form': form})  # return form with errors
    else:
        form = SignUpForm()
        return render(request, 'store/signup.html', {'form': form})  # Ensure GET request returns an HttpResponse

def login_view(request):
    return render(request, 'store/login.html')
