from django.db import models
from web.exceptions.models import NotEnoughQuantityError
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = "Categoria"

class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Marca"

class Size(models.Model):
    size_name = models.IntegerField()  # Cambiado a IntegerField

    def __str__(self):
        return f'{self.size_name}'

class Product(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    UNISEX = 'UNISEX'
    GENERO_CHOICES = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (UNISEX, 'UNISEX')
    ]
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ManyToManyField(Size)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='productos/', null=True, blank=True)
    genre = models.CharField(max_length=10, choices=GENERO_CHOICES)


    def discount_quantity(self, quantity):
        if self.quantity < quantity:
            msg = f'no hay stock disponible para el producto {self.name}'
            raise NotEnoughQuantityError(msg)
        self.quantity -= quantity
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Producto'
