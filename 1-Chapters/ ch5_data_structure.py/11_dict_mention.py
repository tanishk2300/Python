marks = { "harrry":34, "jerry":45, "lilly":94 }
print(marks.keys())# it print the perticular keys 
print(marks.values()) # it print the values .
#marks.clear()
#print(marks)# it help to clear all the value from the set and make a empty set and reprint the set "marks"
#marks.pop("lilly")# to remove a perticular word and a object use pop .
#print(marks)

#marks.popitem()# it help to remove the last value  
#print(marks)
marks.fromkeys("harry",34 ) # here the key and value use in bracket otherwise output type error.
# it creates new dictionary with default values .

print(marks)

marks.setdefault("name","unknown") # in bracket of setdefault the name is replace by unknown in output .

print(marks)


"=============================================="
# another example 
my_dict = {"name": "Tanishk", "age": 20}

# Key already exists
value = my_dict.setdefault("name", "Unknown")
print(value)  # Output: Tanishk

# Key does not exist, will add it
value = my_dict.setdefault("city", "Jaipur")
print(value)  # Output: Jaipur

print(my_dict)
# Output: {'name': 'Tanishk', 'age': 20, 'city': 'Jaipur'}
