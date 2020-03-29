# function decorator is practiced according to
# https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e

# asterisk on args means number of arguments is variable
# double asterisks on kwargs means it stores all undefined parameters
# as a dictionary

def deco(func):
    def wrapper(*args, **kwargs):
        print('--start--')
        func(*args, **kwargs)
        print('--end--')
    return wrapper

@deco
def test():
    print('Hello Decorator')

test()

#-- practice of double asterisks
# https://qiita.com/_rdtr/items/d3bc1a8d4b7eb375c368
# (12 steps to understand Python decorator)
dct = {'x': 1, 'y': 2}
def bar(x,y):
    return x + y

print(bar(**dct))

