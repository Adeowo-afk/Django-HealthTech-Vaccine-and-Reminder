from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .models import MedicationReminder
from .notifications import send_sms_notification, send_email_notification

def check_and_send_reminders():
    """Runs every minute to check if any active reminders match the current time."""
    now = datetime.now().time().replace(second=0, microsecond=0)
    
    # Find active reminders matching the current minute
    due_reminders = MedicationReminder.objects.filter(
        is_active=True,
        reminder_time__hour=now.hour,
        reminder_time__minute=now.minute
    )

    for reminder in due_reminders:
        if reminder.notification_type == 'SMS' and reminder.phone_number:
            send_sms_notification(reminder.phone_number, reminder.medication_name, reminder.scheduled_time)
        elif reminder.notification_type == 'EMAIL' and reminder.user.email:
            send_email_notification(reminder.user.email, reminder.medication_name, reminder.scheduled_time)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_and_send_reminders, 'interval', minutes=1)
    scheduler.start()