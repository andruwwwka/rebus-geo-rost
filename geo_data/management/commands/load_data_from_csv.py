"""Загрузка данных, выгруженных из ГБУ ЯО "ИАЦ "ГИиНС"."""
import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from geo_data.models import Category, GeoObject


class Command(BaseCommand):
    """Команда прогрузки начальных данные о геообъектах."""

    def handle(self, *args, **options):
        """Алгоритм разборки выгрузки."""
        category_mapping = {
            'Аптеки': ['Аптеки.csv', ],
            'Больницы': [
                'Больницы по территориальному признаку.csv',
                'Больницы специализированные.csv'
            ],
            'Детские площадки': [
                'Детские площадки Дзержинский р-н.csv',
                'Детские площадки Заволжский р-н.csv',
                'Детские площадки Кировский р-н.csv',
                'Детские площадки Красноперекопский р-н.csv',
                'Детские площадки Ленинский р-н.csv',
                'Детские площадки Фрунзенский р-н.csv'
            ],
            'Детские сады': ['Детские сады.csv', ],
            'Учреждения дополнительного образования': [
                'Дополнительное образование.csv',
            ],
            'МФЦ': ['МФЦ.csv', ],
            'Остановки': ['Остановки.csv', ],
            'Школы': [
                'Проблемные и потенциально проблемные объекты '
                'строительства.csv',
            ],
            'Проблемные объекты строительства': ['Школы.csv', ]
        }
        for category_name, data_source_file in category_mapping.items():
            category = Category.objects.create(
                name=category_name
            )
            for data_filename in data_source_file:
                file_path = os.path.join(
                    settings.BASE_DIR,
                    'data',
                    data_filename
                )
                with open(file_path) as csv_file:
                    lines = csv.reader(csv_file)
                    for line in lines:
                        GeoObject.objects.create(
                            name=line[0],
                            category=category,
                            latitude=line[1],
                            longitude=line[2],
                        )
