#!/usr/bin/python

# ./getopt_practice.py Hello World -> ['Hello', 'World'] as args
# ./getopt_practice.py -f Hello -l World
#  -> [('-f', 'Hello'), ('-l', 'World')] as opts
# https://www.geeksforgeeks.org/getopt-module-in-python/

import sys
import getopt

def full_name():
    first_name = ""
    last_name  = ""
    argv = sys.argv[1:]

    try:
        opts,args = getopt.getopt(argv, "f:l:")
    except:
        print("Error")
       
    #import pdb;pdb.set_trace()
    for opt,arg in opts:
        if opt in ['-f']:
            first_name = arg
        elif opt in ['-l']:
            last_name = arg
            
    print (first_name + " " + last_name)

full_name()
