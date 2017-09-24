# implementation of Softmax function: Oreilly Deep Learning from scratch p-69

import numpy as np

a = np.array([1010, 1000, 990])

#np.exp(a) / np.sum(np.exp(a))# overflow error

c = np.max(a)
print(a-c)

print(np.exp(a-c) / np.sum(np.exp(a-c)))
