"""Представления для управления категориями."""
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Category
from ..serializers import CategorySerializer


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    """Представление категорий."""

    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
