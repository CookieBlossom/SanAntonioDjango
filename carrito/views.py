from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from pedido.models import CartItem

@login_required
def agregar_al_carrito(request, producto_id):
    producto = Product.objects.get(pk=producto_id)
    cart_item = CartItem(request.user)
    
    # Supongamos que la cantidad se recibe desde el frontend (no mostrado aquí)
    cantidad_seleccionada = request.POST.get('cantidad', 1)
    
    cart_item.agregar(producto, cantidad_seleccionada)
    
    return redirect('carrito')

@login_required
def eliminar_del_carrito(request, producto_id):
    producto = Product.objects.get(pk=producto_id)
    cart_item = CartItem(request.user)
    
    cart_item.eliminar(producto)
    
    return redirect('carrito')

@login_required
def carrito(request):
    cart_item = CartItem(request.user)
    items = cart_item.obtener_items()
    total_items = len(items)
    context = {
        'items': items,
        'total_items': total_items,
    }
    return render(request, 'carrito.html', context)

@login_required
def finalizar_compra(request):
    cart_item = CartItem(request.user)
    if cart_item.finalizar_compra():
        return redirect('compra_exitosa')
    else:
        return redirect('carrito')

@login_required
def limpiar_carrito(request):
    cart_item = CartItem(request.user)
    cart_item.limpiar_carro()
    return redirect('carrito')