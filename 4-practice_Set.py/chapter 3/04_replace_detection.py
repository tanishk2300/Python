
#q=Replace the double space from problem 3 with single spaces.
a=("hey  this  is  me ")
b=" "
print(a)
if "  " in a:
    print("double space is found!!")
elif " " in a:
    print("single space found")

case=a.replace("  ",b)
print(case)
# i did it replace succesfull.
