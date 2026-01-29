# Create a tuple coordinates = (10, 20) and print both elements.
coordinates = (10, 20)

print(coordinates[0])
print(coordinates[1])

# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.(not possible in tupple )

# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.
conlist=list(coordinates)
conlist[0]=50
conlist=tuple(conlist)
print(conlist)