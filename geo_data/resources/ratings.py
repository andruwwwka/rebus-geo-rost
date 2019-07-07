from rest_framework import serializers, mixins
from rest_framework.viewsets import GenericViewSet

from geo_data.models import Polygon


class PolygonSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField()

    class Meta:
        model = Polygon
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PolygonSerializer, self).__init__(*args, **kwargs)
        self.kind = self.context['request'].query_params.get('kind')

    def get_rating(self, obj):
        return obj.get_rating_by_kind(self.kind)


class PolygonViewSet(mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
