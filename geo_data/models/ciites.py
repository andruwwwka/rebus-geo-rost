"""Модель для городов."""
from django.db import models


class City(models.Model):
    """Города."""

    name = models.CharField(
        verbose_name='Наименование',
        max_length=255,
    )
    longitude = models.FloatField(
        verbose_name='Долгота',
    )
    latitude = models.FloatField(
        verbose_name='Широта',
    )
    rating = models.DecimalField(
        verbose_name='Рейтинг',
        max_digits=3,
        decimal_places=1,
        default=10.0,
    )
