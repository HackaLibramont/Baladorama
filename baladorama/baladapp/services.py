from geopy.distance import vincenty
from baladapp.models import Poi

def compute_distance(start, stop):
    start_lat, start_lng = start
    stop_lat, stop_lng = stop
    return vincenty(start, stop).meters

def find_pois(latitude, longitude, radius, poi_type=None):
    results = []
    pois = Poi.objects.all()
    start = (latitude, longitude)
    for poi in pois:
        stop = (poi.latitude, poi.longitude)
        distance = compute_distance(start, stop)
        print "%d - %s" % (distance, radius)
        if int(distance) <= int(radius):
            results.append(poi)
    return results
