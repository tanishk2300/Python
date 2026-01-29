# Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}

# no....
# Because:

# Sets in Python can only contain immutable (unchangeable) elements.

# A list ([1,2]) is mutable, meaning its contents can be changed.

# Therefore, putting a list inside a set will raise a TypeError.

#if Tuples are immutable '(1,2)', so once in the set, they can’t be changed — which is exactly what sets require.

s = {8, 7, 12, "Harry", [1, 2]}  # ❌ This is invalid

s = {8, 7, 12, "Harry", (1, 2)}  # valid 
