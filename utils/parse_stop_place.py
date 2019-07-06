import requests
import xlrd

API_KEY = '2c0f821f-b2c0-4a36-8ac3-b0a97bdbf072'


class StopPlaceXlsParser(object):
    def read(self, filename='/home/konovalov/stop_places.xls'):
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(sheetx=0)
        for row_index in range(1, sheet.nrows):
            print('name: {0}, latitude {1}, longitude {2}'.format(
                sheet.cell(row_index, 1),
                sheet.cell(row_index, 2),
                sheet.cell(row_index, 3),
            ))
        return None


class SportXlsParser(object):
    def read(self, filename='/home/konovalov/sport.xls'):
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(sheetx=0)
        for row_index in range(1, sheet.nrows):
            print('name: {0}, latitude {1}, longitude {2}'.format(
                sheet.cell(row_index, 0),
                sheet.cell(row_index, 1),
                sheet.cell(row_index, 2),
            ))
        return None


class GosMedXlsParser(object):
    def read(self, filename='/home/konovalov/gos_med.xls'):
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(sheetx=0)
        for row_index in range(1, sheet.nrows):
            print('name: {0}, latitude {1}, longitude {2}'.format(
                sheet.cell(row_index, 0),
                sheet.cell(row_index, 1),
                sheet.cell(row_index, 2),
            ))
        return None


class EducationXlsParser(object):
    def read(self, filename='/home/konovalov/education.xls'):
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(sheetx=0)
        for row_index in range(1, sheet.nrows):
            address = 'г. Ярославль, {0} {1}'.format(
                sheet.cell(row_index, 2).value,
                sheet.cell(row_index, 3).value,
            )
            r = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey={0}&format=json&geocode={1}'.format(
                API_KEY,
                address,
            ))
            coords = r.json().get('response').get('GeoObjectCollection').get('featureMember')[0].get('GeoObject').get(
                'Point').get('pos').split(' ')
            org_name = sheet.cell(row_index, 0).value
            print('name: {0}, latitude {1}, longitude {2}, {3}'.format(
                org_name,
                coords[1],
                coords[0],
                'Сад' if 'дошкольн' in org_name else 'Школа',
            ))
        return None


class CultureXlsParser(object):
    def read(self, filename='/home/konovalov/culture.xls'):
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(sheetx=0)
        for row_index in range(1, sheet.nrows):
            address = sheet.cell(row_index, 1).value
            r = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey={0}&format=json&geocode={1}'.format(
                API_KEY,
                address,
            ))
            coords = r.json().get('response').get('GeoObjectCollection').get('featureMember')[0].get('GeoObject').get(
                'Point').get('pos').split(' ')
            print('name: {0}, latitude {1}, longitude {2}'.format(
                sheet.cell(row_index, 0).value,
                coords[1],
                coords[0],
            ))
        return None


if __name__ == "__main__":
    # parser = StopPlaceXlsParser()
    # parser = SportXlsParser()
    # parser = GosMedXlsParser()
    # parser = EducationXlsParser()
    parser = CultureXlsParser()
    parser.read()
