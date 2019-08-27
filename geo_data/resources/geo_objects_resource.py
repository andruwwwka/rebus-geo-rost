from django_filters import rest_framework
from rest_framework import mixins, serializers
from rest_framework.viewsets import GenericViewSet

from geo_data.models import GeoObject


class GeoObjectSerializer(serializers.ModelSerializer):
    """Сериализатор для объектов"""
    class Meta:
        model = GeoObject
        fields = ('name', 'category', 'longitude', 'latitude')


class GeoObjectsFilter(rest_framework.FilterSet):
    """Класс дополнительной фильтрации по категориям через запятую без пробелов"""
    class Meta:
        model = GeoObject
        fields = {
            'category': ['in']
        }


class GeoObjectsViewSet(mixins.ListModelMixin, GenericViewSet):
    """Представление объектов"""
    queryset = GeoObject.objects.all()
    serializer_class = GeoObjectSerializer
    filterset_class = GeoObjectsFilter
