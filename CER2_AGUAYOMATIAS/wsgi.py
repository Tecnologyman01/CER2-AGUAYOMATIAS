import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CER2_APELLIDONOMBRE.settings')

application = get_wsgi_application()
