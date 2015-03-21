from baladapp.services import find_pois, find_walks
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
import json

# Create your views here.

def find_pois_ctrl(request):
    try:
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        radius = request.GET.get('radius')
        pois = find_pois(latitude, longitude, radius)
        data = serializers.serialize('json', pois)
        return HttpResponse(data, content_type='application/json')
    except Exception as e:
        return HttpResponseBadRequest(e)

def find_walks_ctrl(request):
    try:
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        radius = request.GET.get('radius')
        walks = find_walks(latitude, longitude, radius)
        #results = [ob.as_json() for ob in walks]
        #return HttpResponse(json.dumps(results), content_type="application/json")
        data = serializers.serialize('json', walks)
        return HttpResponse(data, content_type='application/json')
    except Exception as e:
        return HttpResponseBadRequest(e)
