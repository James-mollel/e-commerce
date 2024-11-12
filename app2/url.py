from django.urls import path
from . import views

urlpatterns = [
  path('',views.home, name='home-web'),
  path('home-pro-duct29-389-8-82s-s9-s0',views.all_product,name='product-web'),
  path('cart-cart', views.cartItem, name='cart-cart-items'),
  path('search-result', views.searchResult, name='search-result')
]