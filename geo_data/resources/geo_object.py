from rest_framework import mixins, serializers
from rest_framework.viewsets import GenericViewSet

from ..models import GeoObject


class GeoObjectSerializer(serializers.ModelSerializer):
    """Сериализатор для объектов"""
    class Meta:
        model = GeoObject
        fields = ('name', 'category', 'longitude', 'latitude')


class GeoObjectsViewSet(mixins.ListModelMixin, GenericViewSet):
    """Представление объектов"""
    queryset = GeoObject.objects.all()
    serializer_class = GeoObjectSerializer
