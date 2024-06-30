from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

]

# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)