# Python 3.4 or newer
# export  PYTHONTRACEMALLOC=1 is needed before run
import tracemalloc
tracemalloc.start()

# generator practiced with Introducing Python by Oreilly
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

# generator object is generated
ranger = my_range(1,5)

it = iter(ranger)

print (it)       # nothing comes out
print (next(it)) # 1
print (next(it)) # 2
print (next(it)) # 3
print (next(it)) # 4
#print (next(it)) # error / it's hard to detect the last
#note: Equivalent C++ to Python generator pattern
#      is answered in StackOverFlow 9059187

# get the last element of a list; see No.4 of the following
# https://www.geeksforgeeks.org/python-how-to-get-the-last-element-of-list/
test_list = [1,2,3,4,5]
rit = reversed(test_list)
print ("reversed + next applied: ", next(rit))

# https://docs.python.org/ja/3/library/tracemalloc.html
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 1 ]")
for stat in top_stats[:1]:
    print(stat)


