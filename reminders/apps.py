from django.apps import AppConfig


class RemindersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reminders'



from django.apps import AppConfig

class RemindersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reminders'

    def ready(self):
        import os
        # Avoid running scheduler twice when Django autoreloads in development
        if os.environ.get('RUN_MAIN') == 'true':
            from . import scheduler
            scheduler.start()