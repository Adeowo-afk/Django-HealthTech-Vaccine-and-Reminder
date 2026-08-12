import os
from django.core.mail import send_mail
from twilio.rest import Client

def send_sms_notification(to_phone, medication_name, scheduled_time):
    """Sends an SMS reminder using Twilio."""
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    from_phone = os.getenv('TWILIO_PHONE_NUMBER')
    
    if not all([account_sid, auth_token, from_phone]):
        print("Twilio credentials not fully configured.")
        return False

    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"REMINDER: It is time to take your {medication_name} scheduled for {scheduled_time}.",
            from_=from_phone,
            to=to_phone
        )
        print(f"SMS sent successfully: {message.sid}")
        return True
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False


def send_email_notification(to_email, medication_name, scheduled_time):
    """Sends an Email reminder using Django's send_mail."""
    subject = f"Medication Reminder: {medication_name}"
    message = f"Hello,\n\nThis is a friendly reminder to take your {medication_name} scheduled for {scheduled_time}."
    from_email = os.getenv('SENDGRID_FROM_EMAIL', 'noreply@healthtech.com')

    try:
        send_mail(
            subject,
            message,
            from_email,
            [to_email],
            fail_silently=False,
        )
        print(f"Email sent successfully to {to_email}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False