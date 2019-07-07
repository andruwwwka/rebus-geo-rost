from django.db import models


class Polygon(models.Model):
    # Координаты верхнего угла полигона
    lat1 = models.FloatField()
    lon1 = models.FloatField()

    # Координаты нихнего угла полигона
    lat2 = models.FloatField()
    lon2 = models.FloatField()

    def get_rating_by_kind(self, kind=None):
        points = self.points
        if kind:
            points = points.filter(kind=kind)
        return points.count()

