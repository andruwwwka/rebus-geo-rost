from rest_framework import routers

from .resources import TestPolygonViewSet, PolygonViewSet
from .resources.category_resource import CategoryViewSet
from .resources.geo_detail_resource import GeoObjectDetailViewSet
from .resources.geo_objects_resource import GeoObjectsViewSet

router = routers.DefaultRouter()
router.register(r'test', TestPolygonViewSet, 'test')
router.register(r'ratings', PolygonViewSet, 'ratings')
router.register(r'categories', CategoryViewSet, 'categories')
router.register(r'objects', GeoObjectsViewSet, 'objects')
router.register(r'object', GeoObjectDetailViewSet, 'object')

urlpatterns = router.urls
