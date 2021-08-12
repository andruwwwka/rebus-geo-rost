"""Сериалайзеры для настроек категорий по городам."""
from rest_framework import serializers

from ..models import CategoriesSettings


class CategoriesSettingsSerializer(serializers.ModelSerializer):
    """Сериалайзер для настроек категорий."""

    class Meta:
        """Описание метаинформации сериалайзера категорий для городов."""

        model = CategoriesSettings
        fields = '__all__'
