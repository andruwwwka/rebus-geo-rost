from rest_framework import mixins, serializers
from rest_framework.viewsets import GenericViewSet

from ..models import GeoObject


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
