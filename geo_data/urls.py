from rest_framework import routers

from geo_data.resources import TestPoligonViewSet

router = routers.DefaultRouter()
router.register(r'test', TestPoligonViewSet, 'test')

urlpatterns = router.urls