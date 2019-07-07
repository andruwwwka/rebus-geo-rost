from django.db import models

from geo_data.models import Point


class Value(models.Model):
    kind = models.CharField(
        max_length=25,
        choices=Point.KINDS
    )
    first_border = models.FloatField()
    second_border = models.FloatField()
    third_border = models.FloatField()
