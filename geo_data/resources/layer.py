"""Модуль представлений слоев."""
from django.db.models import Prefetch
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ..models import Category, GeoObject
from ..serializers import LayerSerializer


class LayerViewSet(ListModelMixin, GenericViewSet):
    """Представление объектов, разделенных по слоям."""

    serializer_class = LayerSerializer

    def get_queryset(self):
        """Получение списка категорий, которые будут построены в слои."""
        params = self.request.query_params
        category_ids = params.get('categories', [])
        categories = Category.objects.filter(id__in=category_ids)
        coordinate_filters = {
            'longitude_min',
            'longitude_max',
            'latitude_min',
            'latitude_max'
        }
        if all((field in params) for field in coordinate_filters):
            points = GeoObject.objects.filter(
                category_id__in=category_ids,
                longitude__gte=coordinate_filters['longitude_min'],
                longitude__lte=coordinate_filters['longitude_max'],
                latitude__gte=coordinate_filters['latitude_min'],
                latitude__lte=coordinate_filters['latitude_max'],
            )
            categories = categories.prefetch_related(
                Prefetch(
                    'geoobject_set',
                    queryset=points,
                    to_attr='geo_objects'
                )
            )
        else:
            categories = categories.prefetch_related(
                Prefetch('geoobject_set', to_attr='geo_objects')
            )
        return categories

    def list(self, request, *args, **kwargs):
        """Получение списка слоев."""
        return super().list(request, *args, **kwargs)
