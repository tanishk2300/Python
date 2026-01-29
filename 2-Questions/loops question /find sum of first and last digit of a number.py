a=int(input("enter ..."))

last_digit=a%10 #last digit k liye 
first_num=a
while first_num>=10:
    first_num=first_num//10

print("first num ",first_num)

print("last num",last_digit)

sum=first_num+last_digit
print("sum of these no...",sum)
    
