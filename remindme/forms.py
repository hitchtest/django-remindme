from django import forms
from remindme.models import Reminder

class ReminderForm(forms.Form):
    description = forms.CharField()
    when = forms.CharField()
