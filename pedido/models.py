# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from web.models import Product

User = get_user_model()
class Purchase(models.Model):
    PENDING = 'pending'
    CANCELLED = 'cancelled'
    DONE = 'done'
    PURCHASE_STATUSES = [
        (PENDING, 'Pending'),
        (CANCELLED, 'Cancelled'),
        (DONE, 'Done'),
    ]

    date = models.DateField(auto_now_add=True)  # Fecha de compra automática al crear, sin la hora
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario asociado a la compra
    status = models.CharField(max_length=30, choices=PURCHASE_STATUSES, default=PENDING)  # Estado de la compra
    group_id = models.IntegerField(unique=True)  # Campo group_id como entero único

    def __str__(self):
        return f'Purchase #{self.pk} - {self.user}'

    def finalizar_compra(self):
        if self.status == self.PENDING:
            self.status = self.DONE
            self.save()
            
class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.product.name} - {self.quantity} - ${self.price}'

    def save(self, *args, **kwargs):
        if not self.brand:
            self.brand = self.product.brand
        
        if self.quantity == 0:
            self.quantity = self.product.quantity
        
        if self.price == 0.0:
            self.price = self.product.price
        
        super().save(*args, **kwargs)