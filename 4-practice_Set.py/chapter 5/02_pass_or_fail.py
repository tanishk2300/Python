#q=Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

a=int(input("enter your english marks : "))
b=int(input("enter your hindi marks : "))
c=int(input("enter your maths marks : "))
total=a+b+c
percentage=(total/300)*100

if a==33 or b==33 or c==33:
    print("just passesd!")
elif percentage<40:
    print("fail")
else:

    print("win ! ")
    print(f"Total Percentage: {percentage:.2f}%")