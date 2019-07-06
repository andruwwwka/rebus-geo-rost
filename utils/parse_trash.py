import requests
import xlrd

API_KEY = '2c0f821f-b2c0-4a36-8ac3-b0a97bdbf072'


class TrashXlsParser(object):
    def read(self, filename='/home/konovalov/trash.xls'):
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
            org_name = sheet.cell(row_index, 0).value
            print('name: {0}, latitude {1}, longitude {2}'.format(
                org_name,
                coords[1],
                coords[0],
            ))
        return None


class PostXlsParser(object):
    def read(self, filename='/home/konovalov/post.xls'):
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(sheetx=0)
        for row_index in range(1, sheet.nrows):
            address = sheet.cell(row_index, 1).value.split(':')[2]
            r = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey={0}&format=json&geocode={1}'.format(
                API_KEY,
                address,
            ))
            coords = r.json().get('response').get('GeoObjectCollection').get('featureMember')[0].get('GeoObject').get(
                'Point').get('pos').split(' ')
            org_name = sheet.cell(row_index, 0).value
            print('name: {0}, latitude {1}, longitude {2}'.format(
                org_name,
                coords[1],
                coords[0],
            ))
        return None


if __name__ == "__main__":

    # parser = TrashXlsParser()
    parser = PostXlsParser()
    parser.read()
