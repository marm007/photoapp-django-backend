web: gunicorn backend.wsgi
worker: celery -A backend worker -B -l INFO