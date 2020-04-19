"""Представления для управления категориями."""
from rest_framework.viewsets import ModelViewSet

from ..models import Category
from ..serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    """Представление категорий."""

    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
