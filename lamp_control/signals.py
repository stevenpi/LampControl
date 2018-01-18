from django.db.models.signals import post_save
from django.dispatch import receiver

from lamp_control.models import Lamp, Log

@receiver(post_save, sender=Lamp)
def create_lamp_log(sender, **kwargs):
    Log.objects.create(lamp=kwargs["instance"])
