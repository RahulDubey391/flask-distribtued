import os

# Flask config
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')

# Celery config
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'