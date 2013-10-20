#!/usr/bin/python
# -*- coding: utf-8 -*-

#--- Scrape wiktionary word frequency data 
#    to store them to a sqlite database

# parent page:
# http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists

import re
import urllib

if __name__ == "__main__":

    urllist = ["http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/1-10000", "http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/10001-20000", "http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/20001-30000", "http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/30001-40000"]
    allhtml = ''
    # -- joint all webpages in the list --
    for url in urllist:
        f = urllib.urlopen(url)
        allhtml = allhtml + f.read()

    #--- strip all html tags; quoted from O'reilly's 'Collective Intelligence'
    alltxt = re.compile(r'<[^>]+>').sub('', allhtml)
    alllines = alltxt.split('\n')

    #--- to match 3 consecutive lines with number, string, number,
    #    create list of the list of every 3 consecutive lines in text 
    trilines = [alllines[i:i+3] for i,x in enumerate(alllines)
                if len(alllines[i:i+3]) >= 3]
    
    ctr = 0
    for l in trilines:
        #   regular expression for a string only with numbers (or alphabets)
        #-- http://d.hatena.ne.jp/Kmizukix/20090908/1252389597
        if re.match(        '^[0-9]{1,}$', l[0]) and \
                re.match('^[a-zA-Z]{1,}$', l[1]) and \
                re.match('^[0-9|\.]{1,}$', l[2]):
            ctr = ctr + 1
            print ctr, '\t', int(l[0]), '\t', l[1], '\t', float(l[2])
