from api.coordinate import Coordinate
from api.measurement import Measurement

class DistanceCalculator(object):

    def __init__(self, postal_code_database, distance_wizard):

        self.postal_code_database = postal_code_database
        self.distance_wizard = distance_wizard
        self.unit_of_measure = Measurement.MILES

    def calculate_distance(self, origin, destination):

        latitude, longitude = self.postal_code_database.query_coordinate(origin)[0]
        origin = Coordinate(latitude, longitude)
        latitude, longitude = self.postal_code_database.query_coordinate(destination)[0]
        destination = Coordinate(latitude, longitude)

        return self.distance_wizard.calculate_distance(origin, destination, self.unit_of_measure)
