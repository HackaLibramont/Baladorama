from django.db import models
import datetime

# Create your models here.

class Walk(models.Model):
    name = models.CharField(max_length=45, null=True)
    address = models.CharField(max_length=100, null=True)
    start_latitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    start_longitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    stop_latitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    stop_longitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    distance = models.IntegerField(null=True)
    is_for_walker = models.BooleanField(default=False)
    is_for_horse = models.BooleanField(default=False)
    is_for_bike = models.BooleanField(default=False)
    is_for_disabled = models.BooleanField(default=False)
    is_loop = models.BooleanField(default=False)
    description = models.TextField(null=True)
    avg_walker_duration = models.IntegerField(null=True)
    avg_horse_duration = models.IntegerField(null=True)
    avg_bike_duration = models.IntegerField(null=True)
    waypoints = models.TextField(null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())

class City(models.Model):
    name = models.CharField(max_length=100)
    zipcode = models.IntegerField(null=True)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=4, decimal_places=2)
    longitude = models.DecimalField(max_digits=4, decimal_places=2)


class GPX(models.Model):
    name = models.CharField(max_length=100)
    metadata = models.CharField(max_length=200)

class GPXTrack(models.Model):
    name = models.CharField(max_length=100)
    gpx = models.ForeignKey(GPX)

class GPXSegment(models.Model):
    name = models.CharField(max_length=100)
    track = models.ForeignKey(GPXTrack)

class GPXWaypoint(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    segment = models.ForeignKey(GPXSegment)