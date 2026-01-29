menu={'pizza':100,
      'burger':50,
      }
print("welcome to the food ordering system")
print("menu")


print("pizza=100 \nburger=50") 
order_random=0

print("chosse which thing you want to eat ")
a =input("enter your choice=" )
if a in menu:
    order_random+=menu[a]
b=input("you want to eat something else? (y/n)")
ordar_random=1
if b=="y":
    c=input("enter your second choice= ")
    if c in menu:
        order_random+=menu[c]
    else:
        print("sorry we dont have this item")
        print("thank you for your order")
       
    if b =="n":
     print("thank you for your order")
print("you have to pay for your order",{order_random})