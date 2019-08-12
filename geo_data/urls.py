from rest_framework import routers

from geo_data.resources import TestPolygonViewSet, PolygonViewSet
from geo_data.resources.test_categories import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'test', TestPolygonViewSet, 'test')
router.register(r'ratings', PolygonViewSet, 'ratings')
router.register(r'categories', CategoryViewSet, 'categories')

urlpatterns = router.urls