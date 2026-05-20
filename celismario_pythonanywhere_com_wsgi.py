import os
import sys
from pathlib import Path

# Path de tu proyecto
project_home = '/home/CelisMario/online_store_Django/tienda_videojuegos'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Definir que estamos en producción
os.environ['DJANGO_PRODUCTION'] = '1'

# Variables obligatorias de Django
os.environ.setdefault('DJANGO_SETTING_MODULE', 'tienda_videojuegos.settings')

# Aplicación WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application