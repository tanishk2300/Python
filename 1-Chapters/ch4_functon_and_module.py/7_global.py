def sum(a,b):
    print("hey i am summing ")
    c=a+b 
    global z # if we use this global z it will perform as a global variable 
    z=0 # here it show local variable which is workable only in this function 
    return c


z=3 #here it is a global variable which is use only for the function which is under it . 
print(sum(3,12))
print(z)
