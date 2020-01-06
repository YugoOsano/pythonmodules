def ArithmeticalSeries(x):
    if x == 0:
        return 1
    return x + ArithmeticalSeries(x-1)

if __name__ == "__main__":
    print (ArithmeticalSeries(10))

