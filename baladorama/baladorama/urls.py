from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from baladapp.models import Walk, PoiType

# Serializers define the API representation.
class WalkSerializer(serializers.ModelSerializer):
#class WalkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Walk
        fields = ('name', 'start_latitude', 'start_longitude', 'distance', 'is_for_walker', 'is_loop', 'description', 'avg_walker_duration', 'waypoints', 'created_at')
        depth = 1


class PoiTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PoiType
        fields = ('id', 'name', )

# ViewSets define the view behavior.
class WalkViewSet(viewsets.ModelViewSet):
    queryset = Walk.objects.all()
    serializer_class = WalkSerializer

class PoiTypeViewSet(viewsets.ModelViewSet):
    queryset = PoiType.objects.all()
    serializer_class = PoiTypeSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'walks', WalkViewSet)
router.register(r'poi_types', PoiTypeViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baladorama.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pois/find$', 'baladapp.views.find_pois_ctrl'),
    url(r'^walks/find$', 'baladapp.views.find_walks_ctrl'),
)
