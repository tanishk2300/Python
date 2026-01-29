def print_pattern(n):
    for i in range(n,0,-1):
        print('*'*i)
num=int(input("enter the number of lines: "))
print_pattern(num)