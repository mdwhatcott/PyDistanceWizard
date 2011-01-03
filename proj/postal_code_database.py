import sqlite3
import sys

class PostalCodeDatabase:

    def __enter__(self):

        return self

    def __exit__(self, type, value, traceback):

        self.cursor.close()
        if value:
            print value
            return False

        return True

    def __init__(self, sql_statements, path_to_postal_code_data=None):

        self.sql = sql_statements
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()
        self._import_into_database(path_to_postal_code_data)

    def _import_into_database(self, record_file):

        delimiter = ',' if record_file.endswith('.csv') else '\t'
        print 'Creating in-memory table...'
        self.cursor.execute(self.sql.CREATE)
        print 'Importing records',
        with open(record_file) as records:
            for line_number, line in enumerate(records):
                if line_number == 0:
                    continue # ignore the first row which is just the header
                self._show_progress(line_number)
                insert_values = PostalCode(line_number, line.split(delimiter)).sqlite_insert_values()
                self.cursor.execute(self.sql.INSERT, insert_values)

        self.connection.commit()
        print

    def _show_progress(self, line_number):

        if line_number != 0 and line_number % 10000 == 0:
            sys.stdout.write('.')

    def query_coordinate(self, origin):

        self.cursor.execute(self.sql.SELECT, (origin,))
        return self.cursor.fetchall()

    def query_postal_codes_within_boundary(self, boundary):

        self.cursor.execute(self.sql.SELECT_WITHIN, (boundary.south, boundary.north, boundary.west, boundary.east))
        return self.cursor.fetchall()

        
class PostalCode(object):

    def __init__(self, id, values):

        self.id = id
        self.values = list(values)
        self.values[-1] = float(self.values[-1])
        self.values[-2] = float(self.values[-2])

    def sqlite_insert_values(self):

        return tuple([self.id] + self.values)
