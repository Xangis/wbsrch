import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zetaweb.settings')

app = Celery('zetaweb')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def SaveLogEntry(log):
    """
    Asynchronous task to save a search log entry, be it a domain search or regular search.
    """
    log.save()
