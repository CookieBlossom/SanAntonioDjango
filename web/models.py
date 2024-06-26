import datetime
from django.db import models
from web.exceptions.model import NotEnoughQuantityError
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} -> {self.name} '

    class Meta:
        verbose_name = "Categoria"

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} -> {self.name}'

    class Meta:
        verbose_name = "Genero"

class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.id} -> {self.name}'
    
    class Meta:
        verbose_name = "Marca"

class Size(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.id} -> {self.name}'
    

def pathImage(instance, filename):
    if instance.pk is None:
        instance.save
    return f'products/product{instance.id}/{filename}'

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=pathImage, null=True, blank=True)


    def discount_quantity(self, quantity):
        if self.quantity < quantity:
            msg = f'no hay stock disponible para el producto {self.name}'
            raise NotEnoughQuantityError(msg)
        self.quantity -= quantity
    
    def __str__(self):
        return f'{self.id} -> {self.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Volver a guardar si hay una imagen y no tiene la ruta correcta
        if self.image and 'products/product' not in self.image.path:
            self.image.name = pathImage(self, self.image.name)
            super().save(*args, **kwargs)    
    
    class Meta:
        verbose_name = 'Producto'


class Purchase(models.Model):
    PENDING = 'pending'
    CANCELLED = 'cancelled'
    DONE = 'done'
    PURCHASE_STATUSES = [
        (PENDING, 'pending'),
        (CANCELLED, 'cancelled'),
        (DONE, 'done'),
    ]
    
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=PURCHASE_STATUSES, default=PENDING)
    group_id = models.CharField(max_length=100, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
            today = datetime.date.today().strftime('%Y%m%d')
            self.group_id = f'{self.user_id}_{today}'
            super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.user.username} - {self.date.strftime("%Y%m%d")} - {self.id}'

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.ForeignKey(Genre, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.product.name} - {self.quantity} - ${self.price}'