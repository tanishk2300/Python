'''Using format(), create a sentence:
    "My name is John and I am 25 years old."
    by passing "John" and 25 as variables.'''
name="john"
age=27
string="My name is {} and I am {} years old.".format(name,age)

print(string)

# Do the same using f-strings.

print(f"My name is {name} and I am {age} years old.")

