from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from baladapp.models import Walk
from baladapp.models import GPX


# Serializers define the API representation.
class WalkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Walk
        fields = ('name', )


class GPXSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GPX
        fields = ('name', )

# ViewSets define the view behavior.
class WalkViewSet(viewsets.ModelViewSet):
    queryset = Walk.objects.all()
    serializer_class = WalkSerializer

class GPXViewSet(viewsets.ModelViewSet):
    queryset = GPX.objects.all()
    serializer_class = GPXSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'walks', WalkViewSet)
router.register(r'poi_types', PoiTypeViewSet)
router.register(r'gpx', GPXViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baladorama.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pois/find$', 'baladapp.views.find_pois_ctrl'),
)
