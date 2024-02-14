from celery import Celery
from datetime import timedelta
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
celery_app = Celery('Config')
celery_app.autodiscover_tasks()

# celery_app.conf.broker_url =
