def decorator(func):
    def wraper():
            print("I am testing my decorator.")
            func()
            print("succesfull!")
    return wraper
def say_hello():
    print("this side tanishk .")
f=decorator(say_hello)
f()
