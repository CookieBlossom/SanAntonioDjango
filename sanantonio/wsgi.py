"""
WSGI config for sanantonio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line
from .settings import PORT
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sanantonio.settings')

application = get_wsgi_application()



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tu_proyecto.settings')
execute_from_command_line(['manage.py', 'runserver', f'0.0.0.0:{PORT}'])