#**kwarvs:-used to press a variable number of keyword arguments to a function. it collects all the extra named arguments into a dictionary .
#these features allow to functions to be more flexible and handle different numbers of arguments.
def marks(**kwargs):
    # kwargs is a dictionary with all the key value pairs which were passed to marks .
    for item in kwargs.keys():
        print(f"the marks of {item} is {kwargs[item]}")

marks(subham=45, tanishk=90, jack=35, tom=99,)
# here the condition is the args are use at first and than the kwargs are use after it .
