#q=Write a program to print multiplication table of n using for loops in reversed order.
n=int(input('enter a number: '))
print(f"\n multiplication table of {n}")

for i in range(10,0,-1):
    print(f'{n}X{i}={n*i}')
