from rest_framework import routers

from geo_data.resources import TestPolygonViewSet, PolygonViewSet

router = routers.DefaultRouter()
router.register(r'test', TestPolygonViewSet, 'test')
router.register(r'ratings', PolygonViewSet, 'ratings')

urlpatterns = router.urls