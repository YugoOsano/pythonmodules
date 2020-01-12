# practice of @property decorator
# example found at:
# https://www.python.ambitious-engineer.com/archives/344

class Sample:
    def __init__(self):
        self.__text = "sample"

    @property
    def text(self):
        return "({0})".format(self.__text)

    @text.setter
    def text(self, text):
        if text is None:
            self.__text = "None"
        else:
            print("text is set as: ", text)
            self.__text = text

    @text.deleter
    def text(self):
        pass

obj = Sample()
print(obj.text)

obj.text = None
obj.text = "hello"
print(obj.text)

del obj.text
print(obj.text)
