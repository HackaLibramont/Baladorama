from django.db import models

# Create your models here.

class Walk(models.Model):
    name = models.CharField(max_length=45, null=True)
    address = models.CharField(max_length=100, null=True)
    start_latitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    start_longitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    stop_latitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    stop_longitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)

class City(models.Model):
    name = models.CharField(max_length=100)
    zipcode = models.IntegerField(null=True)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=4, decimal_places=2)
    longitude = models.DecimalField(max_digits=4, decimal_places=2)
