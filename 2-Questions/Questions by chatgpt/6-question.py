#Print the multiplication table of a number (entered by user).
n=int(input("enter a number to print a table: "))

for i in range (1,11):
    print(f"{i}*{n}={i*n}")
    
    