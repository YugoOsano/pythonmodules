#!/c/Python27/python
# -*- coding: utf-8 -*-

#-- convert data of a csv file to a sqlite database
#   the example is downloaded from 
#   http://openflights.org/data.html
#   and contains:
#  Airport ID, Name of airport, City, Country, 
#  IATA/FAA3-letter IATA code,Blank if not assigned.
#  ICAO	4-letter ICAO code. Blank if not assigned.
#  Latitude, Longitude, Altitude, Timezone, DST	Daylight savings time


import sys
import sqlite3

def readtext(file1):
    alllines = []
    try:
        with open(file1) as f:
            alltext  = f.read()
            alllines = alltext.split('\n')
    except:
        print "can't open file"
        sys.exit()
    
    return alllines

#-- strip double quotations from words --
def modifylistformat(lines):
    newlines = []
    for l in lines:
        words    = l.split(',')
        if len(words) == 11:
            newlines.append( map(lambda x: x.strip('\"'),words))
    
    return newlines

#-- convert list to database --
def list2db(lines, db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS airports")
    cur.execute(""" 
    CREATE TABLE airports(
    id       INTEGER NOT NULL PRIMARY KEY,
    name     TEXT    NOT NULL,
    city     TEXT    NOT NULL,
    country  TEXT    NOT NULL, 
    iata     TEXT,
    icao     TEXT,
    lat      REAL    NOT NULL,
    lon      REAL    NOT NULL,
    alt      REAL    NOT NULL,
    time     REAL    NOT NULL,
    dst      TEXT    NOT NULL
    )
    """)
    
    for i,l in enumerate(lines):
        #if i < 30:
        try:
            cur.execute("""
            INSERT INTO airports VALUES
            (?,?,?,?,?,?,?,?,?,?,?)
            """, l)
                #con.commit()
        except:
            pass
            #print i, l
    
    dblist = cur.execute("SELECT * FROM airports")
    con.commit()

    #for l in dblist:
    #    print l

    con.close()

if __name__ == "__main__":

    allitemraw = readtext(sys.argv[1])
    allitem    = modifylistformat(allitemraw)

    
    list2db(allitem, sys.argv[2])
    
    #for i,l in enumerate(allitem):
    #    if i < 5:
    #        print l

