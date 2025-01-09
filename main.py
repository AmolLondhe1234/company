# main.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'company.settings')
app = get_wsgi_application()  # This creates the 'app' that Gunicorn is looking for

if __name__ == "__main__":
    from gunicorn.app.wsgiapp import WSGIApplication
    
    port = int(os.environ.get("PORT", 8080))
    options = {
        'bind': f'0.0.0.0:{port}',
        'workers': 2,
        'timeout': 120,
    }
    
    WSGIApplication("%(prog)s [OPTIONS] %s" % "main:app").run()