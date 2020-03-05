# https://towardsdatascience.com/kl-divergence-python-example-b87069e4b810

# numpy can't be run when a file named 'unittest.py' exists
# in the current directory.
# https://stackoverflow.com/questions/10917245/numpy-importerror-cannot-import-name-testcase

import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt

def kl_divergence(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))

