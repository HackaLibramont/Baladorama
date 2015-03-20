from django.core.management.base import BaseCommand
from baladapp.models import GPX, GPXTrack, GPXSegment, GPXWaypoint
from os import listdir
from os.path import isfile, join
import gpxpy

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        #first_arg = args[0]
        mypath = './baladapp/static/gpx/'
        for f in listdir(mypath):
            if isfile(join(mypath, f)):
                self.load_from_file(mypath, f)

    def load_from_file(self, folder_path, file_name):
        gpx_file = open(join(folder_path, file_name), 'r')

        gpx_obj = gpxpy.parse(gpx_file)
        gpx = GPX(
            name=file_name,
        )
        gpx.save()
        for track in gpx_obj.tracks:
            t = GPXTrack(
                name="trackname",
                gpx=gpx,
            )
            gpx.gpxtrack_set.add(t)

            for segment in track.segments:
                s = GPXSegment(
                    name="nope",
                    track=t,
                )
                t.gpxsegment_set.add(s)

                for point in segment.points:
                    p = GPXWaypoint(
                        latitude=point.latitude,
                        longitude=point.longitude,
                        segment=s,
                    )
                    s.gpxwaypoint_set.add(p)