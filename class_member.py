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
    @classmethod
    def SelfName(cls):
        # class member variable can be defined also herein
        cls.number = 1
        
        
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
    