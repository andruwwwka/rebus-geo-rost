from geo_data.models import Point
from utils.base_point_creator import BasePointCreator


class SportsGroundParser(BasePointCreator):
    def fill_points(self):
        sheet = self.get_sheet('../data/....xls')
        for row_index in range(1, sheet.nrows):
            latitude = sheet.cell(row_index, 1).value
            longitude = sheet.cell(row_index, 2).value
            try:
                self.create_point(
                    title=sheet.cell(row_index, 0).value,
                    lat=float(latitude),
                    lon=float(longitude),
                    kind=Point.SPORTS_GROUND,
                    polygon=self.get_polygon(latitude, longitude)
                )
            except Point.DoesNotExist:
                pass
