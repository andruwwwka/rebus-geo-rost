"""Представление для получения геоданных."""
from rest_framework.viewsets import ModelViewSet

from ..models import GeoObject
from ..serializers import GeoObjectSerializer


class GeoObjectsViewSet(ModelViewSet):
    """Представление объектов геоданных."""

    queryset = GeoObject.objects.all()
    serializer_class = GeoObjectSerializer
