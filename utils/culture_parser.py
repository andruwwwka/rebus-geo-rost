from geo_data.models import Point, Polygon
from utils.base_point_creator import BasePointCreator


class CultureParser(BasePointCreator):
    def fill_points(self):
        sheet = self.get_sheet('culture.xls')
        for row_index in range(1, sheet.nrows):
            latitude, longitude = self.api.get_coordinate(sheet.cell(row_index, 1).value)
            try:
                self.create_point(
                    title=sheet.cell(row_index, 0).value,
                    lat=float(latitude),
                    lon=float(longitude),
                    kind=Point.CULTURE,
                    polygon=self.get_polygon(latitude, longitude)
                )
            except Polygon.DoesNotExist:
                pass
