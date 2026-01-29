def uppercast(func):
    def wraper():
        return func().upper()
    return wraper
def mark(func):
    def wrapper():
        return func()+"!!!😋"
    return wrapper

@uppercast
@mark
def name():
    return "💤tanishk"

print(name())
    
