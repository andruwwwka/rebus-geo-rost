"""Модель для категорий объектов."""
from django.db import models


class Category(models.Model):
    """Категории объектов."""

    name = models.CharField(
        verbose_name='Наименование',
        max_length=255,
    )
    radius = models.IntegerField(
        verbose_name='Радиус действия категории в метрах',
        blank=True,
        null=True
    )
    power = models.BooleanField(
        verbose_name='Степень влияния',
        default=True,
    )
    is_active = models.BooleanField(
        verbose_name='Активно',
        default=True,
    )
    debug = models.BooleanField(
        verbose_name='Отладочная категория',
        default=False
    )
