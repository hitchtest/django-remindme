from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from remindme.forms import ReminderForm
from models import Reminder
import parsedatetime
import datetime
import time

def home(request):
    return render_to_response("index.html")

@login_required()
def dashboard(request):
    reminders = Reminder.objects.all()
    return render_to_response("dashboard.html", locals(), context_instance=RequestContext(request))

@login_required()
def create(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            date_and_time = datetime.datetime.fromtimestamp(
                time.mktime(parsedatetime.Calendar().parse(
                    form.cleaned_data['when']
                )[0])
            )
            Reminder.objects.create(
                user = request.user,
                description = form.cleaned_data['description'],
                date_and_time = date_and_time,
            )
            return HttpResponseRedirect("/dashboard")
    else:
        form = ReminderForm()

    return render_to_response("create.html", locals(), context_instance=RequestContext(request))
