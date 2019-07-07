from geo_data.models import Point, Polygon
from utils.base_point_creator import BasePointCreator


class EducationParser(BasePointCreator):
    def fill_points(self):
        sheet = self.get_sheet('education.xls')
        for row_index in range(1, sheet.nrows):
            address = 'г. Ярославль, {0} {1}'.format(
                sheet.cell(row_index, 2).value,
                sheet.cell(row_index, 3).value,
            )
            latitude, longitude = self.api.get_coordinate(address)
            org_name = sheet.cell(row_index, 0).value
            try:
                self.create_point(
                    title=org_name,
                    lat=float(latitude),
                    lon=float(longitude),
                    kind=Point.INFANT_SCHOOL if 'дошкольн' in org_name.lower() else Point.SCHOOL,
                    polygon=self.get_polygon(latitude, longitude)
                )
            except Polygon.DoesNotExist:
                pass
