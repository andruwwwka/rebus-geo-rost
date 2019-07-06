from random import randint

from rest_framework import serializers, mixins
from rest_framework.viewsets import GenericViewSet

from geo_data.models import Poligon


class PoligonSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField()

    class Meta:
        model = Poligon
        fields = '__all__'

    def get_rating(self, obj):
        return randint(1,10)


class TestPoligonViewSet(mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Poligon.objects.all()
    serializer_class = PoligonSerializer
