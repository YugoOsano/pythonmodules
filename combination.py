# https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def posterior_probability (n: int, h: int, q: float)->float:
    return (n+1) * ncr(n,h) * q**h * (1-q)**(n-h)
