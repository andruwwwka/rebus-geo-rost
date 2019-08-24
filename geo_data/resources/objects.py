from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, mixins
from rest_framework.viewsets import GenericViewSet

from geo_data.models import Category, GeoObject


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий"""
    class Meta:
        model = Category
        fields = ('id', 'name', 'radius', 'power')


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
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


class GeoObjectsViewSet(mixins.ListModelMixin, GenericViewSet):
    """Представление объектов"""
    queryset = GeoObject.objects.all()
    serializer_class = GeoObjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GeoObjectsFilter


class GeoObjectDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для отдельного объекта"""
    class Meta:
        model = GeoObject
        fields = '__all__'


class GeoObjectDetailViewSet(mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             GenericViewSet):
    """Представление для отдельного объекта"""

    queryset = GeoObject.objects.all()
    serializer_class = GeoObjectDetailSerializer
