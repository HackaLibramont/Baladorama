from geopy.distance import vincenty
from baladapp.models import Poi, Walk

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
        poi.distance_from = int(distance)
        #print "%d - %s" % (distance, radius)
        if int(distance) <= int(radius):
            results.append(poi)
    return results

def find_walks(latitude, longitude, radius):
    results = []
    walks = Walk.objects.all()
    start = (latitude, longitude)
    for walk in walks:
        stop = (walk.start_latitude, walk.start_longitude)
        distance = compute_distance(start, stop)
        walk.distance_from = int(distance)
        #print "%d - %s" % (distance, radius)
        if int(distance) <= int(radius):
            results.append(walk)
    return results
