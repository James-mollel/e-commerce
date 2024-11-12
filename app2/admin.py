from django.contrib import admin
from .models import Products, QuickLink,UserDetail

# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
  search_fields = ['product_name','selling_price']
  list_display = ['product_name','selling_price','created_at','this_product_available']
  list_filter = ['product_name','selling_price','created_at']


@admin.register(QuickLink)
class QuickLinksAdmin(admin.ModelAdmin):
  list_display = ['platform_name','url']

@admin.register(UserDetail)
class userDetailAdmin(admin.ModelAdmin):
  list_display = ['created','name','email']
  search_fields = ['name','email']
  list_filter = ['created']

