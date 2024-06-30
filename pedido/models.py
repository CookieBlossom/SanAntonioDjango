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

    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=PURCHASE_STATUSES, default=PENDING)
    group_id = models.CharField(max_length=100, editable=False)

    def __str__(self):
        return f'Purchase #{self.pk} - {self.user.username}'

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