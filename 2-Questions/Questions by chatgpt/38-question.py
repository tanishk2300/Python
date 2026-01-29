'''Create a dictionary of three friends and their phone numbers. Use:

    keys() to get all names
    values() to get all numbers
    items() to loop over key-value pairs and print them
'''
friends={"tanishk":"9462016405","me":"9462016005","you":"9462016115"}

# keys() to get all names.
print(friends.keys())
# values() to get all numbers.
print(friends.values())
#  items() to loop over key-value pairs and print them.
for name, values in friends.items():
    print(name,"=>",values)