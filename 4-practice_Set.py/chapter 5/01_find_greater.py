#q=Write a program to find the greatest of four numbers entered by the user.
num1=float(input("enter the number1: "))
num2=float(input("enter the number2: "))
num3=float(input("enter the number3: "))
num4=float(input("enter the number4: "))
# Assume the first number is the greatest initially
greatest=num1
if num2 > greatest:
    greatest = num2 
if num3 > greatest:
    greatest = num3
if num4 > greatest:
    greatest = num4 

print("the greatest number is",greatest)
