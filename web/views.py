from django.shortcuts import render, redirect, get_object_or_404
from carrito.models import ShoppingCart, CartItem
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Product, Category, Brand, Size

@login_required
def home(request):
    user = request.user
    
    try:
        carrito_db = ShoppingCart.objects.get(user=user)
    except ShoppingCart.DoesNotExist:
        carrito_db = ShoppingCart.objects.create(user=user)
    
    carrito_items = CartItem.objects.filter(user=user)

    context = {
        'user': user,
        'carrito_db': carrito_db,
        'carrito_items': carrito_items,
        # Otros datos que desees pasar al template
    }
    return render(request, 'web/home.html', context)

@login_required
def agregar_al_carrito(request, producto_id):
    user = request.user
    producto = get_object_or_404(Product, pk=producto_id)
    
    item_existente = CartItem.objects.filter(user=user, product=producto).first()
    if item_existente:
        item_existente.quantity += 1
        item_existente.save()
    else:
        nuevo_item = CartItem(user=user, product=producto, price=producto.precio)
        nuevo_item.save()
    
    return redirect('home')

@login_required
def finalizar_compra(request):
    user = request.user
    
    carrito_items = CartItem.objects.filter(user=user)
    if carrito_items.exists():
        # Lógica para finalizar la compra (por ejemplo, crear una orden de compra, realizar el pago, etc.)
        
        # Limpiar carrito después de la compra
        carrito_items.delete()
    
    return redirect('home')
@login_required
def products(request):
    productos = Product.objects.all()
    data = list(productos.values())
    return JsonResponse(data, safe=False)

def get_brands(request):
    brands = Brand.objects.all()
    data = list(brands.values())  # Convertir queryset a lista de diccionarios
    return JsonResponse(data, safe=False)


def get_categories(request):
    category = Category.objects.all()
    data = list(category.values())  # Convertir queryset a lista de diccionarios
    return JsonResponse(data, safe=False)
