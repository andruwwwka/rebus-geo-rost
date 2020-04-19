"""Сериалайзеры для геоданных."""
from rest_framework.serializers import ModelSerializer

from ..models import GeoObject


class GeoObjectSerializer(ModelSerializer):
    """Сериалайзер объектов геоданных."""

    class Meta:
        """Описание метаинформации сериалайзера геоданных."""

        model = GeoObject
        fields = "__all__"


class GeoObjectsItemSerializer(ModelSerializer):
    """Сериалайзер геобъекта геоданных в виде элемента набора в словаре."""

    class Meta:
        """Описание метаинформации сериалайзера элемента слоя."""

        model = GeoObject
        fields = (
            'name',
            'longitude',
            'latitude'
        )
