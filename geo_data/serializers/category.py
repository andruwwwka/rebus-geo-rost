"""Сериалайзеры для категорий."""
from rest_framework import serializers

from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериалайзер для категорий."""

    class Meta:
        """Описание метаинформации сериалайзера категорий."""

        model = Category
        exclude = ('is_active', )
