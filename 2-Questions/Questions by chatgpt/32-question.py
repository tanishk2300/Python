'''Start with numbers = [5, 2, 9, 1, 7] and do the following:

    Sort the list in ascending order.
    Append the number 10 to the list.
    Remove the number 2 from the list.
'''
numbers = [5, 2, 9, 1, 7]

# Sort the list in ascending order
numbers.sort()

print(numbers)

# Sort the list in decending order.
numbers.sort(reverse=True)

print(numbers)

#  Append the number 10 to the list.
numbers.append(10)
print(numbers)

#  Remove the number 2 from the list.
numbers.remove(2)
print(numbers)
