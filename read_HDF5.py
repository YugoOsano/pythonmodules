# coding: utf-8
import h5py
f = h5py.File('myfile.h5', 'r')
f['/experiment1'].attrs['date']
y = f['/experiment1/array1']
import numpy as np
a = np.array(y)
f.close()
