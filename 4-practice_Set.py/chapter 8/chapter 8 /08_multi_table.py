#Write a python function to print multiplication table of a given number.
def multi_table(n):

    for i in range(1,11):
        print(f"{n}*{i}={n*i} ")
    return

n=int(input("enter the number: "))
result=multi_table(n)
print(result)
