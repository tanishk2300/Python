# *args:-used to pass a variable number of positional arguments to a function. it collects all the extra arguments into a tuple. 
def sum(*args):
    # arga will be a tuple pf all the values passed to sum .
    total=0
    for item in args: # it make the all number sum at a same time .
        total+=item
    return total 
print(sum(345,30,10,5)) 

