import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ayurvedic_healthcare.settings')

application = get_wsgi_application()

# Add this line
app = application