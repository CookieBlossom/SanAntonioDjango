from django.contrib.auth import get_user_model
from .models import Product
from pedido.models import Purchase, PurchaseItem
User = get_user_model()

class Cart:
    def __init__(self, user=None):
        self.user = user
        self.cart_items = {}

    def agregar_item(self, producto, cantidad=1):
        producto_id = str(producto.id)
        
        if producto_id in self.cart_items:
            self.cart_items[producto_id]['cantidad'] += cantidad
        else:
            self.cart_items[producto_id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'cantidad': cantidad,
                'imagen': producto.imagen.url
            }

    def obtener_items(self):
        productos_ids = self.cart_items.keys()
        productos = Product.objects.filter(id__in=productos_ids)
        
        carrito_items = []
        for producto in productos:
            item_data = self.cart_items[str(producto.id)]
            carrito_items.append({
                'producto': producto,
                'cantidad': item_data['cantidad'],
                'precio_total': float(item_data['precio']) * item_data['cantidad'],
            })
        
        return carrito_items

    def finalizar_compra(self):
        if self.user:
            compra = Purchase.objects.create(user=self.user)
            
            for producto_id, item_data in self.cart_items.items():
                producto = Product.objects.get(pk=producto_id)
                cantidad = item_data['cantidad']
                precio_unitario = float(item_data['precio'])
                total_precio = precio_unitario * cantidad
                
                PurchaseItem.objects.create(
                    purchase=compra,
                    product=producto,
                    brand=producto.brand,
                    quantity=cantidad,
                    price=total_precio
                )
            self.limpiar_carro()
            
            return True

        return False
    

    def limpiar_carro(self):
        self.cart_items = {}

class CartItem:
    def __init__(self, user=None):
        self.user = user
        self.cart = Cart(user)

    def agregar(self, producto, cantidad=1):
        self.cart.agregar_item(producto, cantidad)

    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart.cart_items:
            del self.cart.cart_items[producto_id]

    def obtener_items(self):
        return self.cart.obtener_items()

    def finalizar_compra(self):
        return self.cart.finalizar_compra()

    def limpiar_carro(self):
        self.cart.limpiar_carro()