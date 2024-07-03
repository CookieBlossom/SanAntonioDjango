from django.contrib.auth.decorators import login_required
from carrito.models import CartItem

@login_required
def carrito(request):
    carrito_items = CartItem.objects.filter(user=request.user)
    total_carrito = sum(item.total_price for item in carrito_items)
    
    return {
        'carrito_items': carrito_items,
        'total_carrito': total_carrito,
    }
