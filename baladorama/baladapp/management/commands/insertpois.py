from django.core.management.base import BaseCommand
from baladapp.models import Poi

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        first_arg = args[0]
        poi = Poi(
            name='',
            latitude='',
            longitude='',
        )
        try:
            poi.save()
        except:
            return
