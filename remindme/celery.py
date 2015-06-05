from __future__ import absolute_import

import os

from celery import Celery
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import utc

import datetime

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remindme.settings')


from django.conf import settings

app = Celery('remindme')

app.config_from_object('django.conf:settings')
# Using a string here means the worker will not have to
# pickle the object when using Windows.
#app.config_from_object('django.conf:settings')

#@app.on_after_configure.connect
#def setup_periodic_tasks(sender, **kwargs):
    #sender.add_periodic_task(5.0, send_reminder(), name='remind every 5')


#app.conf.CELERY_RESULT_BACKEND = "redis"

#app.conf.CELERYBEAT_SCHEDULE = {
    #'reminder-every-five-seconds': {
        #'task': 'remindme.celery.send_reminder',
        #'schedule': datetime.timedelta(seconds=5),
        #'args': (),
    #},
#}

#app.conf.BROKER_URL = "redis://localhost:16379/1"

#app.conf.CELERY_RESULT_BACKEND = "redis"

#app.conf.CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

#app.conf.CELERYBEAT_MAX_LOOP_INTERVAL = 5
#app.conf.CELERYBEAT_SYNC_EVERY = 2

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def send_reminders(self):
    from remindme.models import Reminder
    for reminder in Reminder.objects.filter(sent=False).filter(date_and_time__lt = datetime.datetime.now(tz=utc)):
        reminder.sent = True
        reminder.save()
        send_mail("Reminder", reminder.description, "noreply@localhost", ["{} <{}>".format(reminder.user.name, reminder.user.email), ], fail_silently=False)

