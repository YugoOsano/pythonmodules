# coding: utf-8
# iPython data science cookbook 11.1 example

import skimage.exposure as skie
import numpy as np
import matplotlib.pyplot as plt

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

    # ravel: means disentangle the threads or fibers
    # type(img): numpy.ndarray
    # img.ndim -> 2   img.shape -> (288,512) (as tuple)
    # img.ravel().ndim -> 1  img.ravel().shape -> (147456,)

    # histogram plot: range is a tuple of (x.min, x.max)
    # matplotlib.pyplot.hist(x, bins=None, range=None, density=False,
    # weights=None, cumulative=False, bottom=None, histtype='bar',
    # align='mid', orientation='vertical', rwidth=None, log=False,
    # color=None, label=None, stacked=False, *, data=None, **kwargs)
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

    # Python's list can be converted to a numpy array by:
    # xary = numpy.array(alist, dtype=float)
    ax2.hist(img.ravel(), bins=256)

    ax2.set_xlim(0, img.max())
    ax2.set_yticks([])
    
    plt.show()

#img = plt.imread('http://github.com/ipython-books/cookbook-2nd-data/blob/master/beach.png?raw=true')[...,0]
#show(img)

# function to read a vtk file to make histogram
# negative value will be converted to a specified positive one

# vtk file needs to have same number of values in every line as follows
# 1 -1 0 0 2 3
# 1 -1 -1 1 2 0

def bincount_vtk(file: str,
                 x_from_negative: int=0):
   # import pdb; pdb.set_trace()
    raw_ary = np.loadtxt(file)
    ary_int = raw_ary.astype(np.int32)
    ary1d   = ary_int.flatten()
    arypositive = [x if x>= 0 else x_from_negative for x in ary1d]
    bincount = np.bincount(arypositive)
    return bincount

import sys

b = bincount_vtk(sys.argv[1], 5)
print(b)

