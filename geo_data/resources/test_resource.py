from random import randint

from rest_framework import serializers, mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Polygon


class PolygonSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField()

    class Meta:
        model = Polygon
        fields = '__all__'

    def get_rating(self, obj):
        return randint(1, 3)


class TestPolygonViewSet(mixins.ListModelMixin,
                         GenericViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
