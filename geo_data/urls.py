from rest_framework import routers

from .resources import CategoryViewSet, GeoObjectDetailViewSet, GeoObjectsViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, 'categories')
router.register(r'objects', GeoObjectsViewSet, 'objects')
router.register(r'object', GeoObjectDetailViewSet, 'object')

urlpatterns = router.urls
