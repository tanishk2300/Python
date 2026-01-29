#q=Check that a tuple type cannot be changed in python.
a=(1,2,3)
print("tupple=",a)# print tupple to show the tupple 
# ()=tupple 
#[]=list
try: # both try,exept use to prevent from crash .
    a[1]=99 # this is use to change the element '1=99' in tupple cant allow to change and it make a error and jump directly except .
except TypeError as e:# use it to give the error and reason why its tupple 
    print("❌error",e)
    print("yes this is a tupple ")
