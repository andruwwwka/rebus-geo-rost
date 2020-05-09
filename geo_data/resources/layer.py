"""Модуль представлений слоев."""
from django.db.models import Prefetch
from drf_yasg.utils import swagger_auto_schema
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ..models import Category, GeoObject
from ..serializers import LayerListQuerySerializer, LayerSerializer


class LayerViewSet(ListModelMixin, GenericViewSet):
    """Представление объектов, разделенных по слоям."""

    serializer_class = LayerSerializer

    def get_queryset(self):
        """Получение списка категорий, которые будут построены в слои."""
        params = self.request.query_params
        category_ids = params.get('categories', '').split(',')
        categories = Category.objects.filter(id__in=category_ids)
        coordinate_filters = {
            'longitude_min',
            'longitude_max',
            'latitude_min',
            'latitude_max'
        }
        points_filter_params = {'category_id__in': category_ids}
        if all((field in params) for field in coordinate_filters):
            points_filter_params.update(
                {
                    'longitude__gte': params['longitude_min'],
                    'longitude__lte': params['longitude_max'],
                    'latitude__gte': params['latitude_min'],
                    'latitude__lte': params['latitude_max'],
                }
            )
        points = GeoObject.objects.filter(**points_filter_params)
        categories = categories.prefetch_related(
            Prefetch(
                'geoobject_set',
                queryset=points,
                to_attr='geo_objects'
            )
        )
        return categories

    @swagger_auto_schema(
        query_serializer=LayerListQuerySerializer,
    )
    def list(self, request, *args, **kwargs):
        """Получение списка слоев со всеми объектами на них."""
        return super().list(request, *args, **kwargs)
