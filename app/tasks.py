from celery import Celery
from app import app

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def add_task(a, b):
    return a + b

@celery.task
def subtract_task(a, b):
    return a - b