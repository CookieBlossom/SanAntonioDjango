from django.urls import path
from .views import CustomLoginView, products, agregar_al_carrito, get_products_data, get_products, get_brands, get_categories, get_sizes, detalle_producto

urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Utiliza la vista personalizada o la predeterminada
    path('products/', products, name="products"),
    path('api/agregar-al-carrito/<int:producto_id>/<int:quantity>/<int:size_name>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('api/productsData/', get_products_data, name="get_products_data"),
    path('api/products/', get_products, name="get_products"),
    path('api/brands/', get_brands, name='get_brands'),
    path('api/categories/', get_categories, name='get_categories'),
    path('api/sizes/', get_sizes, name='get_sizes'),
    path('api/detalle-producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
]