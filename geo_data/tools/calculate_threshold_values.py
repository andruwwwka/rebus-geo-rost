from geo_data.models import Point, Polygon, Value


class ThresholdValuesCalculator:

    @staticmethod
    def calculate_borders():
        for kinds in Point.KINDS:
            max_count = 0
            for polygon in Polygon.objects.all():
                points_count = polygon.points.filter(kind=kinds[0]).count()
                if points_count > max_count:
                    max_count = points_count
            part = max_count / 3
            Value.objects.get_or_create(
                kind=kinds[0],
                first_border=int(part ** .5),
                second_border=int((part * 2) ** .5),
                third_border=max_count,
            )
