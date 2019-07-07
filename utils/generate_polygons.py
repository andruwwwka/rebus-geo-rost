from itertools import takewhile, count

from geo_data.models import Polygon
from utils.yandex_decoder_wrapper import YandexDecodeApi


class PolygonDataGenerator:

    @staticmethod
    def range_for_float(start, end, step):
        return takewhile(lambda x: x < end, count(start, step))

    @classmethod
    def generate_polygons(cls):
        api = YandexDecodeApi()
        for latitude in cls.range_for_float(57.520544, 57.777502, .010001):
            for longitude in cls.range_for_float(39.695266, 40.027602, .010001):
                coordinate = (latitude + .005000, longitude + .005000)
                if api.get_city(coordinate) == 'Ярославль':
                    Polygon.objects.create(
                        lat1=round(latitude, 6),
                        lon1=round(longitude, 6),
                        lat2=round(latitude + .01, 6),
                        lon2=round(longitude + .01, 6)
                    )
