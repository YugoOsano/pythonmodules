# an example from Effective Python Item 33:
# validate subclasses with metaclasses

# basics about inheritance from type class,
# __new__ method are summarized at:
# https://www.yunabe.jp/docs/python_metaclass.html
class Meta(type):
    # name: name of the class
    # bases: list of base classes
    # class_dict: dict of class attributes
    def __new__(meta, name, bases, class_dict):
        # doubled parenthesis means dealing as a tuple
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)

class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass

class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons needs more sides')
        return type.__new__(meta, name, bases, class_dict)

class Polygon(object, metaclass=ValidatePolygon):
    sides=None

class Triangle(Polygon):
    sides = 3

# ValueError would be raised herein;
# __new__ method is called when defining subclass,
# not when instantiated
class ImaginaryShape(Polygon):
    sides = 2


