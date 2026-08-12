from django.db import models
from django.contrib.auth.models import User

class MedicationReminder(models.Model):
    NOTIFICATION_TYPES = (
        ('EMAIL', 'Email'),
        ('SMS', 'SMS'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    scheduled_time = models.TimeField()
    reminder_time = models.TimeField()
    notification_type = models.CharField(max_length=5, choices=NOTIFICATION_TYPES, default='EMAIL')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Fixed typo here

    def __str__(self):
        return f"{self.user.username} - {self.medication_name}"