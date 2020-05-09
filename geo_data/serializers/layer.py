"""Модуль сериалайзеров слоев."""
from rest_framework import serializers

from ..models import Category
from ..serializers import GeoObjectsItemSerializer


class LayerListQuerySerializer(serializers.Serializer):
    """Сериалайзер для параметров запроса к списку слоев."""
    categories = serializers.ListField(child=serializers.IntegerField())
    longitude_min = serializers.FloatField(required=False)
    longitude_max = serializers.FloatField(required=False)
    latitude_min = serializers.FloatField(required=False)
    latitude_max = serializers.FloatField(required=False)


class LayerSerializer(serializers.ModelSerializer):
    """Сериалайзер для слоя данных."""

    geo_objects = GeoObjectsItemSerializer(many=True, read_only=True)

    class Meta:
        """Описание метаинформации сераиалайзера слоя данных."""

        model = Category
        fields = (
            'id',
            'name',
            'geo_objects'
        )
