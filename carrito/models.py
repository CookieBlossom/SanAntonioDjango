from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from web.models import Product, Size
User = get_user_model()

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Carrito de {self.user.username}'
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'
    
    @property
    def total_price(self):
        total_price = self.quantity * self.price
        return total_price