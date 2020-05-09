"""Сериалайзеры для геоданных."""
from rest_framework import serializers

from ..models import GeoObject


class GeoObjectSerializer(serializers.ModelSerializer):
    """Сериалайзер объектов геоданных."""

    class Meta:
        """Описание метаинформации сериалайзера геоданных."""

        model = GeoObject
        fields = "__all__"


class GeoObjectsItemSerializer(serializers.ModelSerializer):
    """Сериалайзер геобъекта геоданных в виде элемента набора в словаре."""

    class Meta:
        """Описание метаинформации сериалайзера элемента слоя."""

        model = GeoObject
        fields = (
            'name',
            'longitude',
            'latitude'
        )
