def add(a,b):
    x=a+b
    return x


# but here we can also use 
'''def add(a,b):
      return a+b
      '''


c = add(3,5)
print(c)

print("done")
#here now we use the 
def add(a,b,plus=0):
    x=a+b+plus
    return x

c=add(3,4,2)#here we put the valuse 
print(c)

#here we use it like :
def student(name,age):
    print(f"name:{name},age:{age}")

student(age=20,name="bob")