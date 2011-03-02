from proj.postal_code_database import PostalCodeDatabase
from proj.radius_search import RadiusSearch
from api.boundary_wizard import BoundaryWizard
from api.distance_wizard import DistanceWizard
import proj.zip_code_sqlite_statements
import proj.postal_code_sqlite_statements

USA = 'data/5-digit Commercial.csv'
CANADA = 'data/6-digit Commercial.csv'
CANADA_OPTIONS = ['C', '2', 'CA', 'CANADA']

DEFAULT_RADIUS = 4.0
ORIGIN = "\nEnter the origin Postal Code (<ENTER> to quit): "
RADIUS = "Enter the radius in miles: "
RESULTS = "Results within {0} miles of {1}:"
RESULT = "{0:<20}\t\t{1}\t{2}\t{3:f} miles"
POSTAL_CODE = 2
CITY_NAME = 0
STATE = 1
DISTANCE = 3

def main(sql_statements, postal_codes_file_name):
    with PostalCodeDatabase(sql_statements, postal_codes_file_name) as postal_codes:
        searcher = RadiusSearch(postal_codes, BoundaryWizard(), DistanceWizard())
        while True:
            postal_code = raw_input(ORIGIN)
            if not postal_code:
                break
            radius = float(raw_input(RADIUS) or DEFAULT_RADIUS)
            results = searcher.search(postal_code=postal_code, radius=radius)
            report_results(postal_code, radius, results)

def report_results(postal_code, radius, results):

    print RESULTS.format(radius, postal_code)
    for location in results:
        print RESULT.format(location[CITY_NAME], location[STATE], location[POSTAL_CODE], location[DISTANCE])

if __name__ == "__main__":
    data_choice = raw_input('Data: 1. USA or 2. Canada? ').upper()
    data_file = CANADA if data_choice in CANADA_OPTIONS else USA
    sql_statements = proj.postal_code_sqlite_statements if data_file == CANADA else proj.zip_code_sqlite_statements
    main(sql_statements, data_file)
