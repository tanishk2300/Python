#decorator is a function that take a function , it creates a new function inside its body (wrapper). then it returns that new function 
def decorator(func):
   def wrapper():
      print("I am about to executed a function...")
      func()
      print("I have executed this function...") 
   return wrapper
@decorator
def say_hello():
   print("hello!")

say_hello()

'''
f will look something like this 
def f():
   print("i am about to execute a function...")
   print("hello")
   print("i have execute this function...")
   
   '''

#think of a decorator like wrapping a gift:
'''
you “wrap” it with another function that adds extra
 features without changing the original function itself.

 - this is to add 
 def say_hello():
    print("Hello!")

'''


''' to understand in better way 


def my_decorator(func):
    def wrapper():
        # Do something before
        func()
        # Do something after
    return wrapper

@my_decorator
def my_function():
    print("Original function") # this will print which is writen in this 

my_function()# this refers to my function of @ 



'''

# to geet more and add your once 
'''
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
        print("After")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice") 
#output :-
before
hello,alice!
after


#---
🟢 Where do decorators get used?
✅ Logging
✅ Timing code
✅ Access control (checking permissions)
✅ Validation
✅ Properties (like we did in getters & setters)
'''



'''
@property          # makes method behave like an attribute (getter)
@<name>.setter  # makes method behave like an attribute setter

example:-
class MyClass:
    def __init__(self):
        self.__value = 0

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

        
@property
def data(self):
    # When you do obj.data

@data.setter
def data(self, value):
    # When you do obj.data = value

'''