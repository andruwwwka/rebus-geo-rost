import requests
from django.conf import settings

class YandexDecodeApiException(Exception):
    """Возвращается при невозможности получить координаты по адресу"""
    pass


class YandexDecodeApi():

    def __init__(self, format='json'):
        self.api_key = settings.API_KEY
        self.format = format

    def get_response(self, geocode):
        return requests.get(
            f'https://geocode-maps.yandex.ru/1.x/?apikey={self.api_key}&format={self.format}&geocode={geocode}'
        ).json()

    def get_coordinate(self, address):
        response_data = self.get_response(address)
        try:
            longitude, latitude = response_data.get('response').\
                get('GeoObjectCollection').get('featureMember')[0].\
                get('GeoObject').get('Point').get('pos').split(' ')
        except (KeyError, IndexError):
            raise YandexDecodeApiException
        return latitude, longitude

    def get_city(self, coordinate):
        response_data = self.get_response(f'{coordinate[1]},{coordinate[0]}')
        print(response_data)
        try:
            city = ''
            address_components = response_data.get('response'). \
                get('GeoObjectCollection').get('featureMember')[0]. \
                get('GeoObject').get('metaDataProperty').get('GeocoderMetaData'). \
                get('Address').get('Components')
            for component in address_components:
                if component['kind'] == 'locality':
                    city = component['name']
                    break
        except (KeyError, IndexError):
            raise YandexDecodeApiException
        return city
