"""Представления для управления настройками категорий."""
from rest_framework.viewsets import ModelViewSet

from ..models import CategoriesSettings
from ..serializers import CategoriesSettingsSerializer


class CategoriesSettingsViewSet(ModelViewSet):
    """Настройки категорий для городов."""

    serializer_class = CategoriesSettingsSerializer
    queryset = CategoriesSettings.objects.all()
