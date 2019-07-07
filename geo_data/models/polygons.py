from django.db import models


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
        if kinds:
            sum_rating = 0
            for kind in kinds:
                total_count = points.filter(kind=kind).count()
                metrics = Value.objects.get(kind=kind)
                sum_rating += total_count // metrics.part + 1
            rating = round(sum_rating / len(kinds))
        else:
            total_count = points.count()
            metrics = Value.objects.get(kind='all')
            rating = total_count // metrics.part + 1
        return rating

