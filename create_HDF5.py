# coding: utf-8

# HDF5 practice from p-145 IPython data science handbook
import numpy as np
import h5py
f = h5py.File('myfile.h5', 'w')
f.create_group('/experiment1')
f['/experiment1'].attrs['date'] = '2018-01-01'
x = np.random.rand(1000,1000)
f['/experiment1'].create_dataset('array1', data=x)
f.close()
