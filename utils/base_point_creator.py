from abc import abstractmethod, ABCMeta

import xlrd
from django.db.models import Q

from geo_data.models import Point, Polygon
from utils.yandex_decoder_wrapper import YandexDecodeApi


class BasePointCreator:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.api = YandexDecodeApi()

    @staticmethod
    def get_sheet(filename):
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(sheetx=0)
        return sheet

    @staticmethod
    def get_polygon(latitude, longitude):
        polygon = Polygon.objects.get(
            Q(lat1__lte=latitude) & Q(lon1__lte=longitude) & Q(lat2__gte=latitude) & Q(lon2__gte=longitude)
        )
        return polygon

    @staticmethod
    def create_point(**kwargs):
        Point.objects.create(**kwargs)

    @abstractmethod
    def fill_points(self):
        raise NotImplementedError
