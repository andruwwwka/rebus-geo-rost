"""Сериалайзеры для геоданных."""
from rest_framework import serializers

from ..models import GeoObject


class GeoObjectSerializer(serializers.ModelSerializer):
    """Сериалайзер объектов геоданных."""

    class Meta:
        """Описание метаинформации сериалайзера геоданных."""

        model = GeoObject
        fields = "__all__"
