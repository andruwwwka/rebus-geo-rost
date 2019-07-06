from rest_framework import routers

from app_templates.resources.simple import SimpleViewSet

router = routers.DefaultRouter()
router.register(r'test', SimpleViewSet, 'test')

urlpatterns = router.urls