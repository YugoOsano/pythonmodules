#!/c/Python27/python
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


def list2db(lines, db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS airports")
    cur.execute(""" 
    CREATE TABLE airports(
    id  INTEGER NOT NULL
    )
    """)
    

    con.close()

if __name__ == "__main__":

    allitem = readtext(sys.argv[1])

    list2db(allitem, sys.argv[2])
    #for l in allitem:
     #   print l

