from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adl_lrs.settings')

RABBITMQ_USER = os.getenv('RABBITMQ_DEFAULT_USER')
RABBITMQ_PWD = os.getenv('RABBITMQ_DEFAULT_PASS')

RABBITMQ_URL = 'amqp://' + RABBITMQ_USER + ':' + RABBITMQ_PWD + '@rabbitmq:5672/'

from django.conf import settings

app = Celery('lrs',
         broker=RABBITMQ_URL,
         include=['lrs.tasks'])

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
