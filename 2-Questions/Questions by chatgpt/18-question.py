# Take a user input string and check if it is a palindrome (same forwards and backwards).
a=input("enter number to cheak its a palindrom:")

reverse_string=a[::-1]

if a==reverse_string:
    print("its a palidrom ")
else:
    print("its not.")
    