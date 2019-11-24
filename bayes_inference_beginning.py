#!/usr/bin/python3
# coding: utf-8
# this is based on p-244 of IPython data science cookbook
# usage: ./bayes_inference_beginning.py [n of trials] [n of coin front]

import sys
import numpy as np
import matplotlib.pyplot as plt
from combination import posterior_probability

is_args = (len(sys.argv) == 3)

n = int(sys.argv[1]) if is_args else 100
h = int(sys.argv[2]) if is_args else 61

q = np.linspace(0.,1., 1000)

fig, ax = plt.subplots(1,1)
d = posterior_probability(n, h, q)

ax.plot(q,d,'-k')
plt.show()
