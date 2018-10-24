import utm
import requests
import json


class CoordinateHelper:

    def __init__(self):
        pass

    @staticmethod
    def format_lat_long(lat_long):
        rounded_position = (
            round(lat_long[1], 2),
            round(lat_long[0], 2)
        )
        return '{} {}'.format(*rounded_position)

    @staticmethod
    def utm_with_offset(point, offset_east, offset_north):
        """
        Returns a new UTM coordinate offset by the specified distance

        :param point: UTM coordinate to offset
        :param offset_east: Number of meters to add to the easting value
        :param offset_north: Number of meters to add to the northing value
        :return:
        """
        return (
            point[0] + offset_east,
            point[1] + offset_north,
            point[2],
            point[3]
        )


class ElevationData:

    def __init__(self, origin):
        """
        Helper object for querying GeoGratis CDEM API

        :param origin: A tuple representing the lat-long of the point of origin
        """
        self.origin = origin
        self.base_url = 'http://geogratis.gc.ca/services/elevation/cdem/'
        self.profile_url = 'profile?path=LINESTRING({}, {})&steps=100'
        self.altitude_url = 'altitude?lat={}&lon={}'
        self.current_location_base = utm.from_latlon(*self.origin)

    def get_extrapolated_elevation(self, point_1, point_2):
        request_url = self.base_url + self.profile_url.format(
            CoordinateHelper.format_lat_long(point_1),
            CoordinateHelper.format_lat_long(point_2)
        )
        r = requests.get(request_url)
        print(r.text)

    def get_elevation_at_point(self, utm_point):
        point = utm.to_latlon(*utm_point)
        request_url = self.base_url + self.altitude_url.format(
            *point
        )
        r = requests.get(request_url)
        data = json.loads(r.text)
        return data['altitude']


    def get_scan_line(self, line_origin, length, spacing):
        """
        Returns a series of Lat/Long coordinates for points along a line
        segment originating at line_origin and terminating length meters north

        :param line_origin: a UTM coordinate for the start of the line.
        :param length:
        :param spacing:
        :return:
        """
        points = [
            CoordinateHelper.utm_with_offset(
                line_origin, 0, x*spacing
            ) for x in range(int(length/spacing))
        ]
        return points

    def get_elevation_grid(self, east_steps, north_steps, scan_increment):
        for east_index in range(east_steps):
            north_scan = [
                self.get_elevation_at_point(point) for point in
                self.get_scan_line(
                    self.current_location_base,
                    scan_increment * north_steps,
                    scan_increment
                )
            ]
            print(north_scan)
            CoordinateHelper.utm_with_offset(
                self.current_location_base,
                scan_increment,
                0
            )




def main():
    scan_line_length = 1000
    scan_line_increments = 25
    yam_lat_long = (51.125857, -115.119302)
    yam = ElevationData(yam_lat_long)
    # elevations = [
    #     elevation.get_elevation_at_point(x) for x in
    #     elevation.get_scan_line(
    #         elevation.current_location_base,
    #         scan_line_length,
    #         scan_line_increments
    #     )
    # ]
    yam.get_elevation_grid(40,20,25)

def test():
    # Locate Mt Yamnuska
    yam = (51.125857, -115.119302)

    # Convert coordinates to UTM; break them up for some clarity
    yam_utm = utm.from_latlon(*yam)
    easting = yam_utm[0]
    northing = yam_utm[1]

    # Create UTM-looking tuples for utm module of a point and a point x meters north
    x = 10
    p1 = (easting, northing, yam_utm[2], yam_utm[3])
    p2 = (easting, northing + x, yam_utm[2], yam_utm[3])

    p1_lat_long = utm.to_latlon(*p1)
    p2_lat_long = utm.to_latlon(*p2)

    elevation = ElevationData(yam)
    # elevation.get_extrapolated_elevation(p1_lat_long, p2_lat_long)

if __name__ == '__main__':
    main()
