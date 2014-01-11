#!/usr/bin/python
# -*- coding: utf-8 -*-

# scrape html from lecture notes of statistics

# This first scrapes link list in:
# http://www.snap-tck.com/room04/c01/stat/stat0001.html
# then scrapes their content and save them into files.

from BeautifulSoup import BeautifulSoup
import urllib
import re

if __name__ == "__main__":

    urllist = "http://www.snap-tck.com/room04/c01/stat/stat0001.html"
    f    = urllib.urlopen(urllist)
    soup = BeautifulSoup(f)

    #-- Use set to skip repeated links --
    urlset = set()

    #-- extract text within <a> - </a> --
    for link in soup.findAll('a'):
        url = link['href']

        #-- extract urls ending with 'stat****.html' (* is digit) --
        if re.search('stat\d{4}.html$', url):
            urlset.add('http://www.snap-tck.com/room04/c01/stat' +
                       url.strip('.'))

    for url in urlset:
        #-- file name is the end of url --
        filename = re.search('stat\d{4}.html$', url).group()
        try:
            with open(filename, mode='w') as fwrite:
                print filename, url
                fread = urllib.urlopen(url)
                html  = fread.read()
                fwrite.write(html)
        except:
            print url + 'can not open.'

