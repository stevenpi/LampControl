import RPi.GPIO as gpio
from django.db.models.signals import post_save
from django.dispatch import receiver

from lamp_control.models import Lamp, Log


@receiver(post_save, sender=Lamp)
def create_lamp_log(sender, **kwargs):

    lamp = kwargs["instance"]

    gpio.setmode(gpio.BCM)
    gpio.setup(lamp.gpiopin, gpio.OUT)

    if lamp.is_on:
        gpio.output(lamp.gpiopin, gpio.HIGH)
    else:
        gpio.output(lamp.gpiopin, gpio.LOW)

    Log.objects.create(lamp=lamp)
