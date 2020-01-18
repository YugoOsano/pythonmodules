# coding: utf-8
# iPython data science cookbook 11.4 example
# to extract point of interest (POI)

# in iPython, following command let the image pop up
# and any image process can be followed.
# %run -i image_point_of_interest.py
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import skimage
import skimage.feature as sf

img = plt.imread('http://github.com/ipython-books/cookbook-2nd-data/blob/master/child.png?raw=true')

def show(img, cmap=None):
    cmap = cmap or plt.cm.gray
    fig, ax = plt.subplots(1,1,figsize=(8,6))
    ax.imshow(img, cmap=cmap)
    ax.set_axis_off()
    return ax

#show(img)

# source code of the function is available with
# descriptive comments
# /usr/local/lib/python3.5/dist-packages/skimage/feature/
corners = sf.corner_harris(img[:, :, 0])
show(corners)
