from django.contrib import admin
from django.urls import path, include  # Importa 'include' para incluir URLs de otras aplicaciones
from web import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración de Django
    path('', views.home, name="home"),  # URL para la vista principal de tu aplicación
    path('web/', include('web.urls')),  # Reemplaza 'accounts.urls' con el nombre de tu aplicación y archivo 'urls.py'
]

# Configuración para servir archivos estáticos durante el desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
