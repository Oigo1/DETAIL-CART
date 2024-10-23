from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page route
    path('product/<str:sku>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<str:sku>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<str:sku>/', views.remove_from_cart, name='remove_from_cart'),
    path('delete_from_cart/<str:sku>/', views.delete_from_cart, name='delete_from_cart'),
]