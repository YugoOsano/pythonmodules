# coding: utf-8
a = 2
f = lambda x: x+a
print(f(10))
a = 20
print(f(10))

# anonymous use (like C++ [](){}())
result = (lambda x: x+a)(50)
print("anonymous ", result)

# multiple statements in a lambda are not permitted in Python
# https://stackoverflow.com/questions/28429680/lambda-and-multiple-statements-in-python
fmulti = lambda x: (x+2, x+2)
print ("fmulti ", fmulti(100)) #-> (102, 102) will be returned
