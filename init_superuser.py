import os
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()

username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'blossom')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'blossom@example.com')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', '123')

if not User.objects.filter(username=username).exists():
    try:
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superusuario '{username}' creado con éxito.")
    except IntegrityError:
        print(f"El superusuario '{username}' ya existe.")
else:
    print(f"El superusuario '{username}' ya existe.")