from itertools import takewhile, count

from geo_data.models import Poligon


class PoligonDataGenerator:

    @staticmethod
    def range_for_float(start, end, step):
        return takewhile(lambda x: x < end, count(start, step))

    @classmethod
    def generate_poligons(cls):
        for latitude in cls.range_for_float(57.520544, 57.777502, .005001):
            for longitude in cls.range_for_float(39.695266, 40.027602, .005001):
                poligon = Poligon(
                    x1=round(latitude, 6),
                    y1=round(longitude, 6),
                    x2=round(latitude + .005, 6),
                    y2=round(longitude + .005, 6)
                )
                poligon.save()
