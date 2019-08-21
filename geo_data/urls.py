from rest_framework import routers

from geo_data.resources import TestPolygonViewSet, PolygonViewSet
from geo_data.resources.objects import CategoryViewSet, GeoObjectsViewSet, GeoObjectDetailViewSet


router = routers.DefaultRouter()
router.register(r'test', TestPolygonViewSet, 'test')
router.register(r'ratings', PolygonViewSet, 'ratings')
router.register(r'categories', CategoryViewSet, 'categories')
router.register(r'objects', GeoObjectsViewSet, 'objects')
router.register(r'object', GeoObjectDetailViewSet, 'object')

urlpatterns = router.urls
