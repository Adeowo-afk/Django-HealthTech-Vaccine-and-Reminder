from django import forms
from .models import MedicationReminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = MedicationReminder
        fields = '__all__'





        from django import forms
from .models import MedicationReminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = MedicationReminder
        fields = ['medication_name', 'dosage', 'scheduled_time', 'reminder_time', 'notification_type', 'phone_number', 'is_active']
        widgets = {
            'medication_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Amoxicillin'}),
            'dosage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 500mg'}),
            'scheduled_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'reminder_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'notification_type': forms.Select(attrs={'class': 'form-select'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1234567890'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }