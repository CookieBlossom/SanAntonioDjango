from django.contrib import admin
from .models import ShoppingCart, CartItem

@admin.register(ShoppingCart)
class ShoppingCart(admin.ModelAdmin):
    list_display = ('user', 'created_at')

@admin.register(CartItem)
class CartItem(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'price')