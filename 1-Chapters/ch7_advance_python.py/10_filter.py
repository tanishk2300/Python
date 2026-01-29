#here we write the function to choose the number 
#filter()=filter elements from an iterable based on a condition.

def is_greater_and_equal_than_9(x):
    if x>=9:
        return True
    else:
        return False
    
a=[1,2,3,4,5,223,36,6,7,43434,54,8,9]
new=list(filter(is_greater_and_equal_than_9,a))# insted the "is_greater_and_equal_than_9" we can use 'lambda x: x>=9' if we not going to use the function .
print(new)