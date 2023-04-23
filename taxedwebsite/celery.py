import os

# from decouple import config
from celery import Celery

# DJANGO_SETTINGS_MODULE= 'taxedwebsite.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'taxedwebsite.settings')
app = Celery("taxedwebsite")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()