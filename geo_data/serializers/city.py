"""Сериалайзеры для городов."""
from rest_framework import serializers

from ..models import City


class CitySerializer(serializers.ModelSerializer):
    """Сериалайзер для городов."""

    class Meta:
        """Описание метаинформации сериалайзера городов."""

        model = City
