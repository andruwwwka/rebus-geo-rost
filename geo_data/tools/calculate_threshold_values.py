from geo_data.models import Point, Polygon, Value


class ThresholdValuesCalculator:

    @staticmethod
    def calculate_max_values_and_parts():
        total_count = 0
        for kinds in Point.KINDS:
            max_count = 0
            for polygon in Polygon.objects.all():
                points_count = polygon.points.filter(kind=kinds[0]).count()
                if points_count > max_count:
                    max_count = points_count
            part = max_count / 3
            total_count += max_count
            Value.objects.get_or_create(
                kind=kinds[0],
                max_count=max_count,
                part=part
            )
        part = total_count / 3
        Value.objects.get_or_create(
            kind='all',
            max_count=total_count,
            part=part
        )
