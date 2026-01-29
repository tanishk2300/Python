# here we talk about the map 
#map()=transform each element in an iterable using a given function. 
# the map() function applies  given function to each item of an iterable and return an iterators that yields the results.
numbers=[1,2,3,45,21]
# here we want square of these no..

# def square(x):
#     return x*x  # here we make a function to convert those into square 


# here if we use the "lambda x: x*x" it give the same result .
new=list(map(lambda x: x*x ,numbers)) # here we use the 'list' to make it in a list and get the result  
print(new)




