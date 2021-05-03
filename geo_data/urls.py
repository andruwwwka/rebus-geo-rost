"""Роутинг приложения геоданных."""
from rest_framework import routers

from .resources import (
    CategoryViewSet,
    CategoriesSettingsViewSet,
    CityViewSet,
    GeoObjectsViewSet,
    LayerViewSet,
)

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, 'categories')
router.register(r'categories_settings', CategoriesSettingsViewSet, 'categories_settings')
router.register(r'cities', CityViewSet, 'cities')
router.register(r'objects', GeoObjectsViewSet, 'objects')
router.register(r'layers', LayerViewSet, 'layers')

urlpatterns = router.urls
