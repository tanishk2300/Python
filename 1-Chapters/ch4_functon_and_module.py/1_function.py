a=4 
b=2
c=1

average=(a+b+c)/3.0
print(average)

a1=5
b1=3
c1=6
average1=(a1+b1+c1)/3
print(average1)

#use of 'def' who define the function 
def average(a,b,c):
    d=(a+b+c)/3
    #print(d) #if we use print we get output=none 
    return d #if we use return the o1,o2 will return to the 'd' value and give the output .

     


o1=average(3,5,1)
o2=average(4,2,1)

print(o1)
print(o2)

#list method 
#• l1.sort(): updates the list to [1,2,7,8,15,21]
#• l1.reverse(): updates the list to [15,21,2,7,8,1]
#• l1.append(8): adds 8 at the end of the list
#• l1.insert(3,8): This will add 8 at 3 index
#• l1.pop(2): Will delete element at index 2 and return its value.
#• l1.remove(21): Will remove 21 from the list.