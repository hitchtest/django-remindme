from django.core.management.base import BaseCommand
from remindme.celery import send_reminders

class Command(BaseCommand):
    def handle(self, *args, **options):
        send_reminders.delay()
