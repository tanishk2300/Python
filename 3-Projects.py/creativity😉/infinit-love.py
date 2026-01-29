def repeat(n):
    def decorator(func):
        def wraper(a):
            for _ in range(n):
                func(a)
        return wraper
    return decorator

@repeat(11)
def virus(name):
    print(f"Love U.....{name}.")

virus("your name.")





