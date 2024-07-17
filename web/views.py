from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from carrito.models import ShoppingCart, CartItem
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Brand, Size
from .forms import ContactoForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.views import LoginView
import json

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        serializable_context = {k: v for k, v in context.items() if isinstance(v, (str, int, float, list, dict))}
        print("Contexto de login (serializable):", json.dumps(serializable_context, indent=4))  # Depuración
        return context
    
 
@login_required
def home(request):
    if request.user.is_authenticated:

        user = request.user
        
        try:
            carrito_db = ShoppingCart.objects.get(user=user)
        except ShoppingCart.DoesNotExist:
            carrito_db = ShoppingCart.objects.create(user=user)
        
        carrito_items = CartItem.objects.filter(user=user)
        total_carrito = sum(item.total_price for item in carrito_items)

        context = {
            'user': user,
            'carrito_db': carrito_db,
            'carrito_items': carrito_items,
            'total_carrito': total_carrito,
        }
        return render(request, 'web/home.html', context)
    return {}


@login_required
def agregar_al_carrito(request, producto_id, quantity, size_name):
    user = request.user
    producto = get_object_or_404(Product, pk=producto_id)
    size = get_object_or_404(Size, pk=size_name)
    item_existente = CartItem.objects.filter(user=user, product=producto, size=size).first()
    
    if item_existente:
        item_existente.quantity += int(quantity)
        item_existente.save()
    else:
        nuevo_item = CartItem(user=user, product=producto, price=producto.price, quantity=int(quantity), size=size)
        nuevo_item.save()
    
    return JsonResponse({'message': 'Producto agregado al carrito exitosamente'})


@login_required
def finalizar_compra(request):
    user = request.user
    
    carrito_items = CartItem.objects.filter(user=user)
    if carrito_items.exists():
        carrito_items.delete()
    
    return redirect('home')

@login_required
def products(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'products/products.html', context)

@login_required
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Product, pk=producto_id)
    return render(request, 'products/detalle_producto.html', {'producto': producto})

def get_products_data(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()

    products_data = []
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': product.quantity,
            'brand_id': product.brand.id,
            'category_id': product.category.id,
            'description': product.description,
            'genre': product.genre,
            'image_url': request.build_absolute_uri(product.image.url) if product.image else None,
        }
        products_data.append(product_data)

    categories_data = list(categories.values())
    brands_data = list(brands.values())

    data = {
        'products': products_data,
        'categories': categories_data,
        'brands': brands_data
    }

    return JsonResponse(data, safe=False)

def get_products(request):
    product = Product.objects.all()
    data = list(product.values())
    return JsonResponse(data, safe=False)

def get_brands(request):
    brands = Brand.objects.all()
    data = list(brands.values())
    return JsonResponse(data, safe=False)


def get_categories(request):
    category = Category.objects.all()
    data = list(category.values())
    return JsonResponse(data, safe=False)

def get_sizes(request):
    size = Size.objects.all()
    data = list(size.values())
    return JsonResponse(data, safe=False)


@login_required
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado exitosamente"
        else:
            data["form"] = formulario
    return render(request, 'web/contactos.html', data)

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está en uso.')
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Tu cuenta ha sido creada exitosamente, {username}!')
            return redirect('home')  # Cambia 'home' a la URL a la que quieras redirigir después del registro

    return render(request, 'accounts/register.html')