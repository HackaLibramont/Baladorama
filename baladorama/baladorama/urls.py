from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from baladapp.models import Walk, PoiType, Poi, City

# Serializers define the API representation.
class PoiTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoiType
        fields = ('id', 'name')

class PoiSerializer(serializers.ModelSerializer):
    poi_type = PoiTypeSerializer(many=False, read_only=True)
    class Meta:
        model = Poi
        fields = ('id', 'name', 'latitude', 'longitude', 'description', 'website', 'phone', 'poi_type', 'parent_poi_type', 'image_url')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'zipcode', 'country')

class WalkSerializer(serializers.ModelSerializer):
    pois = PoiSerializer(many=True, read_only=True)
    class Meta:
        model = Walk
        fields = ('name', 'start_latitude', 'start_longitude', 'distance', 'is_for_walker', 'is_loop', 'description', 'avg_walker_duration', 'waypoints', 'created_at', 'pois', 'q_nature', 'q_heritage', 'q_food', 'q_culture', 'weight')
        #depth = 1

# ViewSets define the view behavior.
class WalkViewSet(viewsets.ModelViewSet):
    queryset = Walk.objects.all()
    serializer_class = WalkSerializer

class PoiTypeViewSet(viewsets.ModelViewSet):
    queryset = PoiType.objects.all()
    serializer_class = PoiTypeSerializer

class PoiViewSet(viewsets.ModelViewSet):
    queryset = Poi.objects.all()
    serializer_class = PoiSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'walks', WalkViewSet)
router.register(r'poi_types', PoiTypeViewSet)
router.register(r'pois', PoiViewSet)
router.register(r'cities', CityViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baladorama.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pois/find$', 'baladapp.views.find_pois_ctrl'),
    url(r'^walks/find$', 'baladapp.views.find_walks_ctrl'),
    url(r'^walks/search$', 'baladapp.views.search_walks_ctrl'),
)
