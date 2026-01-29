#q=Write a recursive function to calculate the sum of first n natural numbers.
def sum_of_natural(n):
    if n==1:
        return 1
    else:
        return n+sum_of_natural(n-1)
num=int(input("enter a positive integer: "))
if num>0:
    total=sum_of_natural(num)
    print(f"sum of first{num} natural number is: {total}")
else:
    print("please enter a positive number: ")