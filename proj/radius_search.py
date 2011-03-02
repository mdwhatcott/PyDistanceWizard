import operator
from api.coordinate import Coordinate
from api.measurement import Measurement


class RadiusSearch():
    
    def __init__(self, database, boundary_wizard, distance_wizard):

        self.database = database
        self.boundary_wizard = boundary_wizard
        self.distance_wizard = distance_wizard
        self.unit_of_measure = Measurement.MILES

    def search(self, postal_code, radius):
        
        origin = self._calculate_origin_coordinate(postal_code)
        locations_within_boundary = self._get_locations_within_boundary(origin, radius)
        return self._get_locations_within_radius(origin, locations_within_boundary, radius)

    def _calculate_origin_coordinate(self, postal_code):
        
        originPostalData = self.database.query_coordinate(postal_code)[0]
        latitude = originPostalData[0]
        longitude = originPostalData[1]
        return Coordinate(latitude, longitude)
        
    def _get_locations_within_boundary(self, origin, radius):
        
        boundary = self.boundary_wizard.calculate_boundary(origin, radius, self.unit_of_measure)
        return self.database.query_postal_codes_within_boundary(boundary)
    
    def _get_locations_within_radius(self, origin, locations_within_boundary, radius):
        
        locations_within_radius = self._assemble_locations_within_radius(origin, locations_within_boundary, radius)
        return self._sort_locations_found(locations_within_radius)
    
    def _assemble_locations_within_radius(self, origin, locations_within_boundary, radius):
        
        locations_within_radius = []
        
        for location in locations_within_boundary:
            distance = self._distance_from(origin, location)
            if distance <= radius:
                locations_within_radius.append(self._formatted_location(location, distance))
        
        return locations_within_radius
    
    def _distance_from(self, origin, location):
        
        relative = Coordinate(location[-2], location[-1])
        return self.distance_wizard.calculate_distance(origin, relative, self.unit_of_measure)
    
    def _formatted_location(self, location, distance):
        
        location = list(location) # from tuple to list, so we can append the distance later.
        location.append(distance)
        del location[3:5] # remove unnecessary lat/lon data for report
        return location
    
    def _sort_locations_found(self, locationsFound):
        
        sort_by_distance_index = -1
        return sorted(locationsFound, key=operator.itemgetter(sort_by_distance_index))
