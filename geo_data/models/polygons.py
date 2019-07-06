from django.db import models


class Polygon(models.Model):
    # Координаты верхнего угла полигона
    lat1 = models.FloatField()
    lon1 = models.FloatField()

    # Координаты нихнего угла полигона
    lat2 = models.FloatField()
    lon2 = models.FloatField()
