# coding: utf-8
# this is from p-248 of IPython data science cookbook
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
df = pd.read_csv('https://github.com/ipython-books/cookbook-2nd-data/blob/master/federer.csv?raw=true', parse_dates=['start date'], dayfirst=True)
npoints = df['player1 total points total']
points = df['player1 total points won'] / npoints
aces = df['player1 aces'] / npoints
fig, ax = plt.subplots(1,1)
ax.plot(points, aces, '.')
ax.set_xlim(0.,1.)
ax.set_ylim(0.)
plt.show()
df_bis = pd.DataFrame({'points': points, 'aces': aces}).dropna()
df_bis.corr()
