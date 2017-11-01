# test function
def Calc (x, y):
    return x * 10 + y

# keyword only argument (enforced keyword)
def CalcEnforceKey(x, *, y=5):
    return x * 10 + y

# star arg (let it be optional)
def log(message, *value):
    if not value:
        print (message)
    else:
        values_str = ','.join(str(x) for x in value)
        print ('%s: %s' % (message, values_str))


if __name__ == '__main__':

    # keyword argument test
    print (Calc (3, 4))

    print (Calc (x=3, y=4)) #34
    print (Calc (y=3, x=4)) #43

    # keyword enforced
    #print (CalcEnforceKey (3, 4))#error
    print (CalcEnforceKey (5, y=6))

    
    log('Hello', [0,1,2])
    log('hello')
    
    
