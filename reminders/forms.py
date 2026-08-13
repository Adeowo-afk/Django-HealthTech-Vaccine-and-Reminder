from django import forms
from .models import VaccineReminder  # Make sure this matches your model name in models.py

class ReminderForm(forms.ModelForm):
    class Meta:
        model = VaccineReminder
        fields = '__all__'