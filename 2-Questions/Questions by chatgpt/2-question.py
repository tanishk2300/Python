'''
#Q2: Take two numbers from the user and print their:
 Sum
 Difference
 Multiplication
 Division
'''
import math

a=int(input("enter first number="))
b=int(input("enter second number="))
print("choose what u wanna be sum,sub,divide,multiply")

def calculater(a,b):
    c=input("enter yr choice ")
    if c=="+":
            print(f"the result:{a+b}")
    elif c=="-":
            print(f"the result:{a-b}")
    elif c=="*":
            print(f"the result:{a*b}")
    elif c=="/":
            print(f"the result:{a/b}")
    else:
            print("there was an error")
            return calculater

print=calculater(a,b)
