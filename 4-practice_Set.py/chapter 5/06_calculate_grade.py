marks=int(input("enter your marks u get: "))

if marks>=90 and marks<=100:
    gread = 'ex'
elif marks>=80 and marks<=90:
    gread = 'A'
elif marks>=70 and marks<=80:
    gread = 'B'
elif marks>=60 and marks<=70:
    gread = 'C'
elif marks>=50 and marks<=60:
    gread = 'D'
elif marks>=0 and marks<=50:
    gread = 'F'
else:
    print("no entry")
print("your grade is:" , gread)