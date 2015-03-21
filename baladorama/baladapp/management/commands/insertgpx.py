from django.core.management.base import BaseCommand
from baladapp.models import Walk
from os import listdir
from os.path import isfile, join
import gpxpy
import random

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        mypath = './baladapp/static/gpx/'
        for f in listdir(mypath):
            if isfile(join(mypath, f)):
                self.load_from_file(mypath, f)

    def load_from_file(self, folder_path, file_name):
        print file_name
        gpx_file = open(join(folder_path, file_name), 'r')

        gpx_obj = gpxpy.parse(gpx_file)
        for route in gpx_obj.routes:
            waypoints = []
            for point in route.points:
                waypoints.append({"latitude": "%s" % point.latitude, "longitude": "%s" % point.longitude})
            walk = Walk(
                name=file_name.replace("_gpx", "").replace(".GPX",""),
                start_latitude=waypoints[0]['latitude'],
                start_longitude=waypoints[0]['longitude'],
                stop_latitude=waypoints[-1]['latitude'],
                stop_longitude=waypoints[-1]['longitude'],
                waypoints=waypoints.__str__().replace('\'', '\"'),
                avg_walker_duration=random.random() * 300,
                distance=random.random() * 30,
            )
            walk.save()
