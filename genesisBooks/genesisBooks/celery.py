import os
from celery import Celery

# set the default DJANGO settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE','genesisBooks')
# create an instance of the application
app = Celery('genesisBooks')
app.config_from_object()
