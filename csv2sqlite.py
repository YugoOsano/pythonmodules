#!/usr/bin/python
# -*- coding: utf-8 -*-

#-- convert data of a csv file to a sqlite database

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

#-- create list of list --
def modifylistformat(lines):
    newlines = []
    for l in lines:
        words    = l.split('\t')
        newlines.append(words)
#-- strip double quotations from words --
 #       if len(words) == 11:
 #           newlines.append( map(lambda x: x.strip('\"'),words))
    
    return newlines

#-- convert list to database --
#   sql commands are based on English Word Rank data
#   fetched from Wiktionary word frequency list
def list2db(lines, db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS wordrank")
    cur.execute(""" 
    CREATE TABLE wordrank(
    id       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    rank     INTEGER NOT NULL,
    word     TEXT    NOT NULL,
    count    REAL    NOT NULL
    )
    """)
    
    for i,l in enumerate(lines):
       #if i < 30:
        try:
            #--- strip space from each word; not escape sequence like '\s'
            lmodified = [int(l[1]), l[2].strip(' '), float(l[3])]
            cur.execute("""
            INSERT INTO wordrank(rank, word, count) VALUES
            (?,?,?)
            """, lmodified)
                #con.commit()
        except:
            pass
            #print i, l
    
    dblist = cur.execute("SELECT * FROM wordrank")
    con.commit()

    #for l in dblist:
    #    print l

    con.close()

if __name__ == "__main__":

    allitemraw = readtext(sys.argv[1])
    allitem    = modifylistformat(allitemraw)
    
    list2db(allitem, sys.argv[2])
    
#    for i,l in enumerate(allitem):
    #    if i < 5:
#        print l

#   the example is downloaded from 
#   http://openflights.org/data.html
#   and contains:
#  Airport ID, Name of airport, City, Country, 
#  IATA/FAA3-letter IATA code,Blank if not assigned.
#  ICAO	4-letter ICAO code. Blank if not assigned.
#  Latitude, Longitude, Altitude, Timezone, DST	Daylight savings time

#    CREATE TABLE airports(
#    id       INTEGER NOT NULL PRIMARY KEY,
#    name     TEXT    NOT NULL,
#    city     TEXT    NOT NULL,
#    country  TEXT    NOT NULL, 
#    iata     TEXT,
#    icao     TEXT,
#    lat      REAL    NOT NULL,
#    lon      REAL    NOT NULL,
#    alt      REAL    NOT NULL,
#    time     REAL    NOT NULL,
#    dst      TEXT    NOT NULL
