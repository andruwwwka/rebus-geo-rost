from rest_framework import routers

from geo_data.resources import TestPolygonViewSet

router = routers.DefaultRouter()
router.register(r'test', TestPolygonViewSet, 'test')

urlpatterns = router.urls