#Write a program to find whether a given number is prime or not.
def prime(n):
    if n<=1:
        return False # 0 and 1 are not prime numbers
    if n==2:
        return True  # 2 is the only even prime number
    if n%2==0:
        return False # eliminate even numbers greater than 2
     # check for factors from 3 to sqrt(n)
    for i in range(3 ,int(n**0.5)+ 1,2):
        if n%i==0:
            return False
        return True

#  Input from user
a=int(input("enter the number: "))
#cheack and display result
if prime(a):
    print(f"{a} is a prime number.")
else:
    print("its not a prime number.")    
