"""Сериалайзеры для категорий."""
from rest_framework.serializers import ModelSerializer

from ..models import Category


class CategorySerializer(ModelSerializer):
    """Сериалайзер для категорий."""

    class Meta:
        """Описание метаинформации сериалайзера категорий."""

        model = Category
        exclude = ('is_active', )
