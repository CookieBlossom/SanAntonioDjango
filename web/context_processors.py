from carrito.models import ShoppingCart, CartItem

def carrito(request):
    context = {}
    if request.user.is_authenticated:
        try:
            carrito_db = ShoppingCart.objects.get(user=request.user)
        except ShoppingCart.DoesNotExist:
            carrito_db = ShoppingCart.objects.create(user=request.user)
        
        carrito_items = list(CartItem.objects.filter(user=request.user))
        total_carrito = sum(item.total_price for item in carrito_items)
        
        context = {
            'carrito_db': carrito_db,
            'carrito_items': carrito_items,
            'total_carrito': total_carrito,
        }
        
        # Depuración adicional
        for key, value in context.items():
            print(f"Contexto del carrito - {key}: {value}")

    return context