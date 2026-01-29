a=int(input("enter ..."))

last_digit=a%10 #last digit k liye 
first_num=a
digit=0
while first_num>=10:
    first_num=first_num//10
    digit+=1

print("first num ",first_num)

print("last num",last_digit)
middle_part=(a%(10**digit)//10)
swapped=(last_digit *(10**digit))+ (middle_part*10) + first_num

if a<0:
    swapped=-swapped

print("swappe number",swapped)


    
