#use of case 
a=int(input("enter a number btw 1 to 10="))
#here 1,3,6 represent the number from the variable a,

match a:
    case 1:
        print("you won a charger")
    case 3:
        print("you won 3$")
    case 6:
        print("the value is 6")
    case _:
        print("better luck ")

