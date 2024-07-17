from django.contrib import admin
from .models import Product, Brand, Category, Size,Contacto
# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size_name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'brand', 'category', 'genre')
    filter_horizontal = ('size',)
    
@admin.register(Contacto)
class ContactoAdmin (admin.ModelAdmin)
    list_display = ('Contacto')