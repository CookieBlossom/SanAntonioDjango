from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('accounts/login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('products/', views.products, name="product"),
    path('api/brands/', views.get_brands, name='get_brands'),
    path('api/categories/', views.get_categories, name='get_categories'),
]

# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)