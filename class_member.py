# https://qiita.com/0xfffffff7/items/6ef16e79fe9886acb3f2

class Widget(object):

    #-- constructor --
    def __init__(self, r, l):

        #-- normal member variables --
        self.rval = r
        self.lval = l

        #-- protected variable --
        self._protected = 15
        
        #-- private variable --
        self.__secret = 5

    # -- public class member variable --
    classVal = 30

    # -- private class variable
    __SecretClassVal = 55

    #-- normal method --
    def Calc(self):
        # a member variable can be defined also herein
        self.top = 10
        return self.rval * self.lval * self.top * self.__secret

    #-- private method --
    def __MyCalc(self):
        print("Private method.")

    #-- class method --
    #   classmethod is often used
    #   when the class is supposed to be imported
    #   as those methods are easily called by a single import statement.
    @classmethod
    def SelfName(cls):
        # class member variable can be defined also herein
        cls.number = 1

    #-- static method --
    #   a static method is just like a function defined
    #   out of a class scope, but has a merit in being overridable.
    #   http://mojix.org/2012/07/21/python-staticmethod
    #   classmethod and staticmethod are similar but different in
    #   usage of entity; classmethod has a reference to
    #   a class object as the first parameter (StackOverFlow 12179271)
    @staticmethod
    def PrintWithOne(s):
        print(s, ' 1')
        
if __name__ == '__main__':

    w = Widget(2,4)

    print (w.lval)
    #print (w.__secret) # error
    #print (w._Widget_protected) # error
    print (w._Widget__secret) # not recommended

    print (w.Calc())

    # print(Widget.number) # error b/c SelfName isn't called yet
    # call a class method
    Widget.SelfName()
    print(Widget.classVal)
    print(Widget.number)
    
    Widget.PrintWithOne('Hello')
