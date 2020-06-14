"""Модель гео-объектов."""
from django.db import models


class GeoObject(models.Model):
    """Объект для отображения."""

    name = models.CharField(
        verbose_name='Наименование',
        max_length=255,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    longitude = models.FloatField(
        verbose_name='Долгота',
    )
    latitude = models.FloatField(
        verbose_name='Широта',
    )
    address = models.TextField(
        verbose_name='Адрес',
        blank=True,
        null=True,
    )
    additional_info = models.TextField(
        verbose_name='Дополнительная информация',
        blank=True,
        null=True,
    )
    debug = models.BooleanField(
        verbose_name='Отладочный объект',
        default=False
    )
