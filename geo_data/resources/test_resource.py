from rest_framework import serializers, mixins
from rest_framework.viewsets import GenericViewSet

from geo_data.models import Poligon


class PoligonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poligon


class PoligonViewSet(mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Poligon.objects.all()
    serializer_class = PoligonSerializer
