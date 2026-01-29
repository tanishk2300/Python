#q=Write a program to store seven fruits in a list entered by the user
# in simple form 
# fruits=[]

# for i in range(7):
#     fruit=input(f"enter the name of fruits{i+1}: . ")
#     fruits.append(fruit)

# print("list of the fruits:",fruits)

# if u want in the def 
def list_fruit():
    fruits=[]
    for i in range(7):
        fruit=input(f"enter the name of fruit{i+1}:")
        fruits.append(fruit)
    return fruits
list=list_fruit()
print("list of the fruit",list)