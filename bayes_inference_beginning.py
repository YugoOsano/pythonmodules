# coding: utf-8
# this is based on p-244 of IPython data science cookbook

import numpy as np
import matplotlib.pyplot as plt
from combination import posterior_probability

n = 100
h = 61
q = np.linspace(0.,1., 1000)

fig, ax = plt.subplots(1,1)
d = posterior_probability(n, h, q)

ax.plot(q,d,'-k')
plt.show()
