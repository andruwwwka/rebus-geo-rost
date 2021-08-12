"""Представления для управления городами."""
from rest_framework.viewsets import ModelViewSet

from ..models import City
from ..serializers import CitySerializer


class CityViewSet(ModelViewSet):
    """Представление городов."""

    quryset = City.objects.all()
    serializer_class = CitySerializer
