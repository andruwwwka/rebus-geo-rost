from django.db import models


class GeoObject(models.Model):
    """
    Объект для отображения
    """
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

    def __str__(self):
        return '{0}({1}/{2})'.format(
            self.name,
            self.longitude,
            self.latitude,
        )

    def __repr__(self):
        return self.__str__()
