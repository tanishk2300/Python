
def divide(a,b):
    try:
        c=a/b
        print(c)

    except Exception as e:
        print(e)
    #this always exicuted no matter if try completely executed or not .
    # finally is write becouse in the function we have to write it we want to write in it only print cant work here .

    finally:
        print("this is always executed ") # it give us the finall line ...

a=int(input("Enter a number 1: "))
b=int(input("Enter a number 2: "))
divide(a,b)