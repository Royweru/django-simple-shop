from django.db import models

class items(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    image = models.CharField(max_length=2038)
    description = models.CharField(max_length=500)