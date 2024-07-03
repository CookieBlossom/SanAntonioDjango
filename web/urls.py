from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('accounts/login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('products', views.products, name="products"),
    path('api/agregar-al-carrito/<int:producto_id>/<int:quantity>/<int:size_name>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('api/productsData/', views.get_products_data, name="get_products_data"),
    path('api/products/', views.get_products, name="get_products"),
    path('api/brands/', views.get_brands, name='get_brands'),
    path('api/categories/', views.get_categories, name='get_categories'),
    path('api/sizes/', views.get_sizes, name='get_sizes'),
    path('api/detalle-producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),

]