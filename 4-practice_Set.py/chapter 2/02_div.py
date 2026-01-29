# here we get remender by simple program 
a=int(input("enter first number: "))
b=int(input("enter sec.. number: "))
# div=a%b
# print(f"by divideing {a} and {b} we get remender = {div}")


# here we use the def function

def get_remender(a,b):
    remender=a%b
    return remender
remender=get_remender(a,b)

print(f"by divideing {a} and {b} we get remender = {remender}")

if ZeroDivisionError():
    print("bhai zero...")

