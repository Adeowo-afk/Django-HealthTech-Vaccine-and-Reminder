from django import forms
from .models import MedicationReminder  # Replace with your actual model name

class ReminderForm(forms.ModelForm):
    class Meta:
        model = MedicationReminder
        fields = '__all__'  # Or list specific fields like ['title', 'reminder_time', 'phone_number']