import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Auto-run migrations on startup (needed for Vercel)
from django.core.management import call_command
call_command('migrate', '--run-syncdb')

application = get_wsgi_application()