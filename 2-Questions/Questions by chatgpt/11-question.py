# Use a while loop to reverse a given number (e.g., 123 → 321).
num=12345
rev=0

while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10

   
print(rev)



