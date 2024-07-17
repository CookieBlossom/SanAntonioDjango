from django.db import models
from django import forms
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
    image = models.ImageField(upload_to='brands/', null=True, blank=True)
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
    

class Contacto(models.Model):
    opciones_consultas = [
    [0,"CONSULTA"],
    [1, "RECLAMO"],
    [2,"SUGERENCIA"],
    [3,"FELICITACIONES"]
    ]
    nombre = models.CharField(max_length=250)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    Avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'tipo_consulta', 'mensaje', 'Avisos']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'tipo_consulta': forms.Select(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
            'Avisos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }