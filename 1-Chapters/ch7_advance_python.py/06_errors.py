# help to tackel through error 
# here we use the while loop to make it in a loop 
# it is an exception handlling in the python .


'''
#while True:
#    try:
#        a=int(input("Enter a number 1: "))
#        b=int(input("Enter a number 2: "))
#        print(f"The div.. of the numb... is {a/b}")
#    except ValueError:
#        print("Please don't perform bad typecasts.")
#    except ZeroDivisionError:
#        print("Hey dont divide by zero.")
#    except Exception as e:
#        print("unknown error occurred.", e)
'''

    
# now here we use the "raise" function which helps to rise the error 
# "like something is wrong" #
a=int(input("Enter a number 1: "))
b=int(input("Enter a number 2: "))
if b==0:
    raise ValueError("Please dont divide by zero.") # here raise use to raise the error and tell there is something wrong with your prog...
print(f"The div.. of the numb... is {a/b}")
#now here it show the error becouse or raise ..

