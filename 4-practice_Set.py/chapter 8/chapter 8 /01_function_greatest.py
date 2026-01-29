#q=Write a program using functions to find greatest of three numbers.
def get_greatest(a,b,c):
    if a>=b and a>=c:
        return a 
    elif b>=a and b>=c:
        return b
    else:
        return c
    
num1=int(input("enter the value of A: "))
num2=int(input("enter the value of B: "))
num3=int(input("enter the value of C: "))

greatest=get_greatest(num1,num2,num3)
print('the gratest number: ',greatest)