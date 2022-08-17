from django.apps import AppConfig
from django.core.signals import request_finished


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals
        # Explicitly connect a signal handler.
        # request_finished.connect(signals.SellarCreated)
        