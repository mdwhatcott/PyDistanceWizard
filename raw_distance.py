from api.coordinate import Coordinate
from api.measurement import Measurement
from api.distance_wizard import DistanceWizard

def main():

    unit_of_measure = Measurement.MILES if \
        raw_input("Unit of measure in (m)iles or (k)ilometers: ") == 'm' else \
        Measurement.KILOMETERS
    origin, destination = get_coordinates()
    wizard = DistanceWizard()
    distance = wizard.calculate_distance(origin, destination, unit_of_measure)
    report(distance, unit_of_measure)

def get_coordinates():

    print "1 - Enter your own data"
    print "2 - Use existing data"
    choice = raw_input("Enter the number of your choice: ")

    return get_user_coordinates() if choice == '1' else use_existing_coordinates()

def get_user_coordinates():

    origin = get_coordinate("\nOrigin")
    destination = get_coordinate("\nDestination")

    return origin, destination

def get_coordinate(coordinate_identifier):

    print "{0} Coordinate".format(coordinate_identifier)
    lat = float(raw_input("Enter the Latitude value: "))
    lon = float(raw_input("Enter the Longitude value: "))

    return Coordinate(lat, lon)

def use_existing_coordinates():

    origin = Coordinate(40.791787, -74.674518)
    destination = Coordinate(40.332324, -75.116759)

    return origin, destination

def report(distance, unit_of_measure):

    print '\nThe distance between your coordinates is: {0} {1}.'.format(distance, formatted_unit_of_measure(unit_of_measure))

def formatted_unit_of_measure(unit_of_measure):

    return 'Miles' if unit_of_measure == Measurement.MILES else 'Kilometers'

if __name__ == "__main__":
    main()
