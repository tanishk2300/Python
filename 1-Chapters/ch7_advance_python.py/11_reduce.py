#reduce()=applies a function cumulatively to the elements of an iterable to reduce it to a single value.
from functools import reduce
number=[1,2,3,4,5,6]
#      [3,3,4,5,6]
#      [6,4,5,6]
#      [10,5,6]
#      [15,6]
#      [21]
# like that this function work 

def sum(a,b):
    return a+b
c=reduce(sum,number)
print(c)
