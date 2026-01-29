# Print the following pattern using a for loop:

for i in range(1,6):
    print("*"*i)

#Print the following reverse pattern using a for loop:
print("\nPrint the following reverse pattern using a for loop:")
for i in range(6,0,-1):
    print("*"*i)

#Print the following Pyramid pattern using a for loop: 
print("the following Pyramid pattern using a for loop:")
rows=5
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2*i + 1))

#Print the following Inverted Pyramid pattern using a for loop: 
print("Print the following Inverted Pyramid pattern using a for loop: ")
rows=5
for i in range(rows):
    print(" " * i + "*"*(2*(rows-i-1)+1))

#Print the following Square pattern using a for loop: 
print("Print the following Square pattern using a for loop: ")
for i in range(5):
    print("*"*5)

#Print the following Hollow Square pattern using a for loop: 
print("Print the following Hollow Square pattern using a for loop: ")
n=5
for i in range(n):
    if i==0 or i==n-1:
        print("*" * n)
    else:
        print("*" +" "*(n-2)+"*")

#Print the following Half Pyramid pattern using a for loop: 
print("Print the following Half Pyramid pattern using a for loop: ")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
