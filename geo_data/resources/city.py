"""Представления для управления городами."""
from rest_framework.viewsets import ModelViewSet

from ..serializers import CitySerializer


class CityViewSet(ModelViewSet):
    """Представление городов."""

    serializer_class = CitySerializer
