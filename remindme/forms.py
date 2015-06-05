from django import forms
from models import Reminder

class ReminderForm(forms.ModelForm):

    class Meta:
        model = Reminder
        exclude = ('sent', 'user', )
