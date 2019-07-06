from geo_data.models import Point
from utils.base_point_creator import BasePointCreator


class BusStationParser(BasePointCreator):

    def fill_points(self):
        sheet = self.get_sheet('../data/bus_stations.xls')
        for row_index in range(1, sheet.nrows):
            latitude = sheet.cell(row_index, 2).value
            longitude = sheet.cell(row_index, 3).value
            self.create_point(
                title=sheet.cell(row_index, 1).value,
                lat=float(latitude),
                lon=float(longitude),
                kind=Point.BUS_STATION,
                polygon=self.get_polygon(latitude, longitude)
            )
