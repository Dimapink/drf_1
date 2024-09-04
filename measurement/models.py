from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)




class Sensor(models.Model):
    name = models.CharField(max_length=255, verbose_name="name")
    description = models.TextField(max_length=255, verbose_name="description")


class Measurement(models.Model):
    sensor = models.ForeignKey(to=Sensor, related_name='measurements', on_delete=models.CASCADE, verbose_name="sensor")
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)