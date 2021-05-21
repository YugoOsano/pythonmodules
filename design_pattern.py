# factory
class A:
    def hello(self):
        print("hello A")

class B:
    def hello(self):
        print("hello B")

def factory(is_a: bool):
    if (is_a): return A()
    return B()

for is_a in [True, False]:
    c = factory(is_a)
    print(type(c))
    c.hello()

# functor
class F:
    def __init__(self, name: str):
        self.name = name
    def __call__(self, n: int):
        for i in range(n):
            print(self.name)

#f = F() # error
f = F('hoge')
f(5)

# like C/C++ struct (Stackoverflow 35988)
from collections import namedtuple
MyStruct = namedtuple("MyStruct", "x y z is_exist")

m = MyStruct(1,3,4,True)
print(m)
print(m.x, m.is_exist)
# m.x = 20 # error of 'can't set attribute'

