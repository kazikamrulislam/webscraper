#/quotescraper/celery.py
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotescraper.settings')

celery_app = Celery("quotescraper")

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.config_from_object("django.conf:settings", namespace="CELERY")

celery_app.conf.update( # New setting for Celery 6.0 and above
    broker_url='redis://localhost:6380/0',  
    broker_connection_retry=True,  
    broker_connection_retry_on_startup=True  # New setting for Celery 6.0 and above
)

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()