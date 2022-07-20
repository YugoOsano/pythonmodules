# enum practice referencing
# https://www.geeksforgeeks.org/enum-in-python/

import typing
import enum

# definition needed on every item unlike C++
class UserList(enum.Enum):
    one = 1
    two = 2
    three = 3

def ReturnMap(files: list)->dict:
    a = {0:[], 1:[]}
    return a

l=['aaa', 'bbb']
ReturnMap(l)

print (UserList.one) # UserList.one
print (repr(UserList.one))
print (type(UserList.one))
print (UserList.one.name)

# own enum member
class ItemHolder:
    def __init__(self,
                 item: UserList):
        self.item = item

ih = ItemHolder(UserList.two)
print (ih.item)
