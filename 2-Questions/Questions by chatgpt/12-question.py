# Use a for loop to reverse a given number (e.g., 123 → 321).
num=123
rev=""
num_str=str(num)



for i in range(len(num_str)-1,-1,-1):
    rev+=num_str[i]
    
rev=int(rev)
print("reverse number",rev)

    