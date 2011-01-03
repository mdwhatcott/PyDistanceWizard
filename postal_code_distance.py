from proj.postal_code_database import PostalCodeDatabase
from DistanceWizard.distance_wizard import DistanceWizard
from proj.distance_calculator import DistanceCalculator
import proj.zip_code_sqlite_statements
import proj.postal_code_sqlite_statements

USA = 'data/5-digit Commercial.csv'
CANADA = 'data/6-digit Commercial.csv'
CANADA_OPTIONS = ['C', '2', 'CA', 'CANADA']

ORIGIN = "Enter the origin Postal Code (<ENTER> to quit): "
DESTINATION = "Enter the destination Postal Code (<ENTER> to quit): "
RESULT = 'Distance between {0} and {1} is {2}\n'

def main(sql_statements, data_file_name):
    with PostalCodeDatabase(sql_statements, data_file_name) as postal_codes:
        calculator = DistanceCalculator(postal_codes, DistanceWizard())
        perform_calculations(calculator)

def perform_calculations(calculator):
    while True:
        origin, destination = raw_input(ORIGIN), raw_input(DESTINATION)
        if not origin or not destination:
            break
        distance = calculator.calculate_distance(origin, destination)
        print RESULT.format(origin, destination, distance)

if __name__ == '__main__':
    data_choice = raw_input('Data: 1. USA or 2. Canada? ').upper()
    data_file = CANADA if data_choice in CANADA_OPTIONS else USA
    sql_statements = proj.postal_code_sqlite_statements if data_file == CANADA else proj.zip_code_sqlite_statements
    main(sql_statements, data_file)