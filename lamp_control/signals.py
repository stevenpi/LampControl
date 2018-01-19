from django.db.models.signals import post_save
from django.dispatch import receiver
from gpiozero import LED

from lamp_control.models import Lamp, Log


@receiver(post_save, sender=Lamp)
def create_lamp_log(sender, **kwargs):

    lamp = kwargs["instance"]
    led = LED(lamp.gpiopin)
    if lamp.is_on:
        led.off()
    else:
        led.on()

    Log.objects.create(lamp=lamp)
