from rest_framework import routers

from .resources import TestPolygonViewSet, PolygonViewSet
from .resources.category import CategoryViewSet
from .resources.geo_detail import GeoObjectDetailViewSet
from .resources.geo_object import GeoObjectsViewSet

router = routers.DefaultRouter()
router.register(r'test', TestPolygonViewSet, 'test')
router.register(r'ratings', PolygonViewSet, 'ratings')
router.register(r'categories', CategoryViewSet, 'categories')
router.register(r'objects', GeoObjectsViewSet, 'objects')
router.register(r'object', GeoObjectDetailViewSet, 'object')

urlpatterns = router.urls
