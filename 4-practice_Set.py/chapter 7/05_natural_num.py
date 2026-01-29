#Write a program to find the sum of first n natural numbers using while loop.
a= int(input("enter a number: "))
i=1
total=0
while i<=a:
    total+=i
    i+=1
print(f"the sum of the first{a} natural number is: {total}")