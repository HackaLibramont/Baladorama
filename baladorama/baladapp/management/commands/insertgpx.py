from django.core.management.base import BaseCommand
from baladapp.models import GPX, GPXTrack, GPXSegment, GPXWaypoint

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        #first_arg = args[0]
        gpx = GPX(
            name="testGPX",
            metadata="testmetadata"
        )
        try:
            gpx.save()
        except:
            return
