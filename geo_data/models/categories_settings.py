"""Модель настроек категорий для городов."""
from django.db import models


class CategoriesSettings(models.Model):
    """Настройки категорий для городов."""

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    city = models.ForeignKey(
        'City',
        on_delete=models.CASCADE,
    )
    radius = models.IntegerField(
        verbose_name='Радиус действия категории в метрах',
    )
