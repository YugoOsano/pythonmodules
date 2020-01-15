# coding: utf-8
# iPython data science cookbook 11.1 example

import skimage.exposure as skie
import numpy as np
import matplotlib.pyplot as plt
img = plt.imread('http://github.com/ipython-books/cookbook-2nd-data/blob/master/beach.png?raw=true')[...,0]

def show(img):
    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,3))
    ax1.imshow(img, cmap=plt.cm.gray)
    ax1.set_axis_off()

    ax2.hist(img.ravel(), lw=0, bins=256)
    ax2.set_xlim(0, img.max())
    ax2.set_yticks([])
    
    plt.show()

show(img)

