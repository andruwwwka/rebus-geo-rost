"""Представления для управления категориями."""
from rest_framework.viewsets import ModelViewSet

from ..models import Category
from ..serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    """Представление категорий."""

    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer

    def get_queryset(self):
        """Получение списка категорий."""
        categories = super().get_queryset()
        params = self.request.query_params
        if not params.get('debug'):
            categories.filter(debug=False)
        return categories
