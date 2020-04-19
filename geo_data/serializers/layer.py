"""Модуль сериалайзеров слоев."""
from rest_framework.serializers import ModelSerializer

from ..models import Category
from ..serializers import GeoObjectsItemSerializer


class LayerSerializer(ModelSerializer):
    """Сериалайзер для слоя данных."""

    geo_objects = GeoObjectsItemSerializer(many=True, read_only=True)

    class Meta:
        """Описание метаинформации сераиалайзера слоя данных."""

        model = Category
        fields = (
            'name',
            'geo_objects'
        )
