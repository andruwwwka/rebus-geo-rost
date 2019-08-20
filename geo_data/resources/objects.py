from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, mixins, generics
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from geo_data.models import Category, GeoObject


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий"""
    class Meta:
        model = Category
        fields = ('id', 'name', 'radius', 'power')


class CategoryViewSet(ReadOnlyModelViewSet,
                      generics.ListAPIView):
    """Представление категорий"""
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class GeoObjectSerializer(serializers.ModelSerializer):
    """Сериализатор для объектов"""
    class Meta:
        model = GeoObject
        fields = ('name', 'category', 'longitude', 'latitude')


class GeoObjectsFilter(rest_framework.FilterSet):
    """Класс дополнительной фильтрации по категориям
        Перечисление через запятую без пробелов"""
    class Meta:
        model = GeoObject
        fields = {
            'category': ['in']
        }


class GeoObjectsViewSet(mixins.ListModelMixin,
                        GenericViewSet):
    """Представление объектов"""
    queryset = GeoObject.objects.all()
    serializer_class = GeoObjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GeoObjectsFilter
