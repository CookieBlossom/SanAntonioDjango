from django.shortcuts import render
from carrito.models import ShoppingCart  # Asumiendo que ShoppingCart es tu modelo de carrito en models.py
from carrito.carrito import Cart  # Ajusta la importación según la estructura de tu proyecto

def home(request):
    user = request.user
    if user.is_authenticated:
        try:
            carrito_db = ShoppingCart.objects.get(user=user)
            carrito_memoria = Cart(user=user)
        except ShoppingCart.DoesNotExist:
            carrito_db = ShoppingCart.objects.create(user=user)
    else:
        carrito_db = None
        carrito_memoria = Cart(user=None)

    context = {
        'user': user,
        'carrito_db': carrito_db,
        'carrito_memoria': carrito_memoria,
        # Otros datos que desees pasar al template
    }
    return render(request, 'web/home.html', context)