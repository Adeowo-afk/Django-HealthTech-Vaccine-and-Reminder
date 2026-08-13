from django import forms
from .models import MedicationReminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = MedicationReminder
        fields = '__all__'