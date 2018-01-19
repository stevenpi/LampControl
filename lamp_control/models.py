from django.db import models


class Lamp(models.Model):
    name = models.CharField(max_length=64)
    is_on = models.BooleanField(default=False)
    gpiopin = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Log(models.Model):
    lamp = models.ForeignKey("Lamp", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, editable=True)
    hostname = models.CharField(max_length=256)
    description = models.TextField()

    # def __str__(self):
    #
