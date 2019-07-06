import requests
from django.conf import settings

class YandexDecodeApiException(Exception):
    """Возвращается при невозможности получить координаты по адресу"""
    pass


class YandexDecodeApi():

    def __init__(self, format='json'):
        self.api_key = settings.API_KEY
        self.format = format

    def get_coordinate(self, address):
        response_data = requests.get(
            f'https://geocode-maps.yandex.ru/1.x/?apikey={self.api_key}&format={self.format}&geocode={address}'
        ).json()
        try:
            longitude, latitude = response_data.get('response').\
                get('GeoObjectCollection').get('featureMember')[0].\
                get('GeoObject').get('Point').get('pos').split(' ')
        except (KeyError, IndexError):
            raise YandexDecodeApiException
        return latitude, longitude
