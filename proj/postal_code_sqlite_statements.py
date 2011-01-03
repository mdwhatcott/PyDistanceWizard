CREATE = """CREATE TABLE PostalCodes
    (
        ID INTEGER,
        PostalCode TEXT,
        CityName TEXT,
        CityType TEXT,
        ProvinceName TEXT,
        ProvinceAbbr TEXT,
        AreaCode TEXT,
        TimeZone TEXT,
        DST TEXT,
        Latitude REAL,
        Longitude REAL
    )
"""

INSERT = """
INSERT INTO PostalCodes
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
        ?
     )
"""

SELECT = """SELECT Latitude, Longitude
              FROM PostalCodes
             WHERE PostalCode=?
               AND CityType='D'
             LIMIT 1
"""

SELECT_WITHIN = """SELECT CityName,
                   ProvinceAbbr,
                   PostalCode,
                   Latitude,
                   Longitude
              FROM PostalCodes
             WHERE Latitude BETWEEN ? AND ?
               AND Longitude BETWEEN ? AND ?
               AND Latitude != 0
               AND Longitude != 0
"""