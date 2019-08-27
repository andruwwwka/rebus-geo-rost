from rest_framework import mixins, serializers
from rest_framework.viewsets import GenericViewSet

from geo_data.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий"""
    class Meta:
        model = Category
        exclude = ('is_active', )


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    """Представление категорий"""
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
