from celery_worker import celery
from app.tasks import add_task, subtract_task

@celery.task
def add(a, b):
    return add_task.delay(a, b).get()

@celery.task
def subtract(a, b):
    return subtract_task.delay(a, b).get()