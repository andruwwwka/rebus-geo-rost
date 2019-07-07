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
        kind = self.context['request'].query_params.get('kind')
        if kind:
            self.kinds = kind.split(',')
        else:
            self.kinds = []

    def get_rating(self, obj):
        return obj.get_rating_by_kind(self.kinds)


class PolygonViewSet(mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
