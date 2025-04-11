from django.db import models

class MeasurementItem(models.Model):
    temperature = models.DecimalField(max_digits=12, decimal_places=2)
    humidity = models.DecimalField(max_digits=12, decimal_places=2)
    brightness = models.DecimalField(max_digits=12, decimal_places=2, default = 0)
    atmosphericPressure = models.DecimalField(max_digits=12, decimal_places=2, default = 0)
    timestamp = models.DateTimeField(auto_now_add= True)
