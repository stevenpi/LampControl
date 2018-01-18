from django.apps import AppConfig


class LampControlConfig(AppConfig):
    name = 'lamp_control'
    verbose_name = 'Lamp Control'

    def ready(self):
        import lamp_control.signals
