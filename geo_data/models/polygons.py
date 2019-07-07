from django.db import models
from statistics import median

from geo_data.models import Point


class Polygon(models.Model):
    # Координаты верхнего угла полигона
    lat1 = models.FloatField()
    lon1 = models.FloatField()

    # Координаты нихнего угла полигона
    lat2 = models.FloatField()
    lon2 = models.FloatField()

    def get_rating_by_kind(self, kinds=None):
        from geo_data.models import Value
        points = self.points
        ratings = []
        if not kinds:
            kinds = [item[0] for item in Point.KINDS]
        for kind in kinds:
            total_count = points.filter(kind=kind).count()
            metrics = Value.objects.get(kind=kind)
            if total_count < metrics.second_border:
                if total_count < metrics.first_border:
                    ratings.append(1)
                else:
                    ratings.append(2)
            else:
                ratings.append(3)
        return round(median(ratings))

