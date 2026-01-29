# Write a program that counts how many vowels are in a given string.
a=input("enter string to find vowals")
vowals="aeiouAEIOU"
count=0
for char in a:
    if char in vowals:
        count+=1

print("number of vowals",count)