from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseNotFound, HttpResponseRedirect
from forms import ReminderForm
from models import Reminder
import datetime


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
            new_reminder = form.save(commit=False)
            new_reminder.user = request.user
            new_reminder.save()
            return HttpResponseRedirect("/dashboard")
    else:
        form = ReminderForm()

    return render_to_response("create.html", locals(), context_instance=RequestContext(request))
