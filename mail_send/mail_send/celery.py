from __future__ import absolute_import
# Celery Configuration
from celery import Celery
from django.conf import settings
from celery.signals import setup_logging

app = Celery('mail_send')

import os

os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "mail_send.settings"

import django
django.setup()

# Using a string here means the worker doesn't have to serialize
app.config_from_object('django.conf:settings', namespace='CELERY')

@setup_logging.connect
def config_loggers(*args, **kwargs):
    from logging.config import dictConfig
    from django.conf import settings

    dictConfig(settings.LOGGING)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

