from django.db import models
import datetime
import json

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    zipcode = models.IntegerField(null=True)
    country = models.CharField(max_length=100)

class PoiType(models.Model):
    name = models.CharField(max_length=100)

class Poi(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    description = models.TextField(null=True)
    website = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=45, null=True)
    poi_type = models.ForeignKey(PoiType, related_name='child_poi', null=True)
    parent_poi_type = models.ForeignKey(PoiType, related_name='parent_poi', null=True)
    distance_from = models.IntegerField(null=True)

class Walk(models.Model):
    name = models.CharField(max_length=45, null=True)
    address = models.CharField(max_length=100, null=True)
    start_latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    start_longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    stop_latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    stop_longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
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
    pois = models.ManyToManyField(Poi)
    cities = models.ManyToManyField(City, through='Location')
    distance_from = models.IntegerField(null=True)
    q_nature = models.IntegerField(default=0)
    q_heritage = models.IntegerField(default=0)
    q_food = models.IntegerField(default=0)
    q_culture = models.IntegerField(default=0)
    weight = models.IntegerField(null=True)

    def set_waypoints(self, x):
        self.waypoints = json.dumps(x)

    def get_waypoints(self):
        return json.loads(self.waypoints)

    def as_json(self):
        return dict(
            name=self.name

        )

class Location(models.Model):
    is_start = models.BooleanField(default=False)
    is_stop = models.BooleanField(default=False)
    city = models.ForeignKey(City)
    walk = models.ForeignKey(Walk)

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
