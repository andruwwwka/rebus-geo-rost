from rest_framework import serializers, mixins
from rest_framework.viewsets import GenericViewSet

from geo_data.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор"""
    categories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('name', 'radius', 'power')

    def create(self, validated_data):
        category = Category.objects.create(
            name=validated_data['name'],
            radius=validated_data['radius'],
            power=validated_data['power'],
            is_active=True,
        )
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.radius = validated_data.get('radius', instance.radius)
        instance.power = validated_data.get('power', instance.power)
        instance.save()
        return instance


class CategoryViewSet(mixins.ListModelMixin, GenericViewSet):
    """Представление категорий"""
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
