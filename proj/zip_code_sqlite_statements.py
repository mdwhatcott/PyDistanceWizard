CREATE = """CREATE TABLE ZIPCodes
    (
        ID INTEGER,
        ZIPCode TEXT,
        ZIPType TEXT,
        CityName TEXT,
        CityType TEXT,
        CountyName TEXT,
        CountyFIPS TEXT,
        StateName TEXT,
        StateAbbr TEXT,
        StateFIPS TEXT,
        MSACode TEXT,
        AreaCode TEXT,
        TimeZone TEXT,
        UTC REAL,
        DST TEXT,
        Latitude REAL,
        Longitude REAL
    )
"""

INSERT = """INSERT INTO ZIPCodes
                 VALUES
                 (
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?
                 )
"""

SELECT = """SELECT Latitude, Longitude
              FROM ZIPCodes
             WHERE ZIPCode=?
               AND CityType='D'
             LIMIT 1"""

SELECT_WITHIN = """SELECT CityName,
                   StateAbbr,
                   ZIPCode,
                   Latitude,
                   Longitude
              FROM ZIPCodes
             WHERE Latitude BETWEEN ? AND ?
               AND Longitude BETWEEN ? AND ?
               AND Latitude != 0
               AND Longitude != 0"""