#the walrus operator introduced in python 3.8 is an assignment expression operator .
#  it allows you to assign a value to a variable within an expression .
# this can make your code more concise and in some cases more effifient by avoiding repeated calculation or function calls. 
# the name "walrus operator " comes from the operator resemblance to the eye and tusks of a walrus 
# totaly it looks like eye and tusks .
# it is use for make easy from the useless line and unessesary line to make the code harder and complicated insteed these line use the walrus method .

def very_slow_func():
    print("something...")
    print("something...")
    print("something...")
    print("something...")
    print("something...")
    return 70

# if(very_slow_func()>10): # if we use this code it print 'something...' twice 
#     print(very_slow_func())

# a=very_slow_func()    # this function print "something.." original time which mean exeact time .
# if(a>10):              # but there is a better way to do this , by using the walrus operator .
#     print(a)

# this is walrus method
# if((a:=very_slow_func())>10):
#     print(a)
# else:
#     print("it is greater then 10 ")

# this is also a walrus method but in data form , the data collect the data..
while(data:=input("Enter the value: ")):
    print(data)
    if data =="q": # if we write the 'q' then it break (quit) by the command 
        break