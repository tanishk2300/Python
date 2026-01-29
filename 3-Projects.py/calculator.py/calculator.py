try:
    a=int(input("enter the first number: "))
    b=int(input("enter the second number: "))
    print("choose what u wanna do : \nif u wanna add these two number use + \nif u wanna subtract number use -\nif u wanna multiply the numbers use*\nif u wanna divide the numbers use / ")

    c=input("enter your choise:")

          
    if c=="+":
            print(f"the result:{a+b}")
    elif c=="-":
            print(f"the result:{a-b}")
    elif c=="*":
            print(f"the result:{a*b}")
    elif c=="/":
            print(f"the result:{a/b}")
    else:
            print("there was an error")

except Exception as e :
    print("enter a valid number")



