import random
import string

def pass_generate(length):
    characters=string.ascii_letters+string.digits+string.punctuation 

    password =''.join(random.choice(characters)  for _ in range(length))
     
    return password

length=int(input("enter the length; "))

print("pass_generate",pass_generate(length))
