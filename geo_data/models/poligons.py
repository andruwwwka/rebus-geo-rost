from django.db import models


class Poligon(models.Model):
    # Координаты верхнего угла полигона
    x1 = models.FloatField()
    y1 = models.FloatField()

    # Координаты нихнего угла полигона
    x2 = models.FloatField()
    y2 = models.FloatField()
