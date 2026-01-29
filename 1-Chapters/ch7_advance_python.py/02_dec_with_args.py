def repeat(n): # we wrapping things in to which is an another arguement 
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(name):
    print(f"hello! {name}")

'''
def decorator(func):
    def wrapper(name):
        for i in range(n):
            say_hello(name)
    return wrapper
'''    

say_hello('tanu')
