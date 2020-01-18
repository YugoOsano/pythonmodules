# coding: utf-8
# iPython data science cookbook 11.1 example

import skimage.exposure as skie
import numpy as np
import matplotlib.pyplot as plt
img = plt.imread('http://github.com/ipython-books/cookbook-2nd-data/blob/master/beach.png?raw=true')[...,0]

def show(img):
    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,3))
    # (matplotlib) imshow function plots a 2D raster image.
    # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html
    # for the term 'raster image' (=bitmap), see
    # https://en.wikipedia.org/wiki/Raster_graphics
    # raster is originally scanning beam on television
    ax1.imshow(img, cmap=plt.cm.gray)
    ax1.set_axis_off()

    # numpy.ravel() or flatten() function returns one-dimensional array
    # made from all elements of the original multi-dimensional array;
    # a view is returned by ravel() while a copy is returned by flatten().
    ax2.hist(img.ravel(), lw=0, bins=256)
    ax2.set_xlim(0, img.max())
    ax2.set_yticks([])
    
    plt.show()

show(img)

