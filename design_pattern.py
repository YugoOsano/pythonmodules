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

ablist = [factory(True),\
          factory(False)]

#for is_a in [True, False]:
#    c = factory(is_a)
for c in ablist:
    print(type(c))
    c.hello()

# factory 2: see Stackoverflow 372042
class SomeAbstraction:
    pass  # lots of stuff - but missing something
class Mixin1:
    def something(self):
        print("Mixin1")  # one implementation
class Mixin2:
    def something(self):
        print("Mixin2")  # another
class Concrete1(SomeAbstraction, Mixin1):
    pass
class Concrete2(SomeAbstraction, Mixin2):
    pass

def factory_with_abstraction(is1: bool)->SomeAbstraction:
    if (is1): return Concrete1()
    return           Concrete2()

conclist = [factory_with_abstraction(True),\
            factory_with_abstraction(False)]
[conc.something() for conc in conclist]

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

