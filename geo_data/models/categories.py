from django.db import models


class Category(models.Model):
    """
    Категории объектов
    """
    name = models.CharField(
        verbose_name='Наименование',
        max_length=255,
    )
    radius = models.IntegerField(
        verbose_name='Радиус действия категории в метрах',
        blank=True,
    )
    power = models.BooleanField(
        verbose_name='Степень влияния',
        default=True,
    )
    is_active = models.BooleanField(
        verbose_name='Активно',
        default=True,
    )

    def __str__(self):
        return '{0}: {1}({2}м)'.format(
            self.__class__.__name__,
            self.name,
            self.radius,
        )

    def __repr__(self):
        return self.__str__()
