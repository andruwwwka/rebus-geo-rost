from rest_framework import serializers, mixins
from rest_framework.viewsets import GenericViewSet

from geo_data.models import Category, GeoObject


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий"""
    class Meta:
        model = Category
        fields = ('id', 'name', 'radius', 'power')


class CategoryViewSet(mixins.ListModelMixin, GenericViewSet):
    """Представление категорий"""
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class GeoObjectSerializer(serializers.ModelSerializer):
    """Сериализатор для объектов"""
    class Meta:
        model = GeoObject
        fields = ('name', 'category', 'longitude', 'latitude')


class GeoObjectViewSet(mixins.ListModelMixin, GenericViewSet):
    """Представление объектов"""
    queryset = GeoObject.objects.all()
    serializer_class = GeoObjectSerializer
