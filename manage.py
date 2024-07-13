import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sanantonio.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if 'runserver' in sys.argv and not any(arg.startswith('127.0.0.1:') or arg.startswith('0.0.0.0:') for arg in sys.argv):
        port = os.environ.get('PORT', '8000')
        if os.getenv('ENV') == 'production':
            sys.argv.append(f'0.0.0.0:{port}')
        else:
            sys.argv.append(f'127.0.0.1:{port}')
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()