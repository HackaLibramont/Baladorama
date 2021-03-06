from geopy.distance import vincenty
from baladapp.models import Poi, Walk
import sys

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
        waypoints_array = walk.get_waypoints()
        #waypoints_array = []
        #points = walk.waypoints.split(';')
        #for point in points:
            #coordinates = point.split(',')
            #waypoints_array.append(coordinates)
        print waypoints_array
        stop = (walk.start_latitude, walk.start_longitude)
        distance = compute_distance(start, stop)
        walk.distance_from = int(distance)
        #print "%d - %s" % (distance, radius)
        if int(distance) <= int(radius):
            results.append(walk)
    return results

def search_walks(q, min_duration=0, max_duration=sys.maxint, nature_level=0, heritage_level=0, food_level=0, culture_level=0):
    mydict = {'description__icontains': q, 'avg_walker_duration__gte': min_duration, 'avg_walker_duration__lte': max_duration}
    walks = Walk.objects.filter(**mydict)
    results = []
    for walk in walks:
        walk_weight = walk.q_nature*nature_level + walk.q_heritage*heritage_level + walk.q_food*food_level + walk.q_culture*culture_level
        walk.weight = walk_weight
        results.append(walk)
    results.sort(key=lambda x: x.weight, reverse=True)
    return results
