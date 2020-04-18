"""Представление для получения геоданных."""
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import GeoObject
from ..serializers import GeoObjectSerializer


class GeoObjectsViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    """Представление объектов геоданных."""

    queryset = GeoObject.objects.all()
    serializer_class = GeoObjectSerializer
