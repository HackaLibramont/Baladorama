from baladapp.services import find_pois
from django.http import HttpResponse, HttpResponseBadRequest
import json

# Create your views here.

def find_pois_ctrl(request):
    try:
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        radius = request.GET.get('radius')
        pois = find_pois(latitude, longitude, radius)
        return HttpResponse(json.dumps(pois), content_type='application/json')
    except Exception as e:
        return HttpResponseBadRequest(e)
