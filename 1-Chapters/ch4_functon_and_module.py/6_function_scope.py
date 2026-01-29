def sum(a,b):
    #here a and b are local variables 
    c=a+b 
    z=1
    print(z)
    return c

def greet():
    z=32
    print("hellow workd")


z=8 #z is a global variable 
# local variable is that variable which is writen under  the function 
# like 
''' 
def greet():
    print("hellow workd")
this is local variable 

'''
print(z)
print(sum(4,6))
print(z)


# here is example :
print("example:-")
# example of a global variable 
x=10 
def my_func():
    x=5 #local variable 
    print(x)#output :5

my_func()
print(x)    #output 10 here (global x remains unchaneged )



