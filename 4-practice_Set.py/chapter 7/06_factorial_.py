#Write a program to calculate the factorial of a given number using for loop.
# Take input from user
n = int(input("Enter a number: "))

# Initialize factorial to 1
factorial = 1

# Use for loop to multiply numbers from 1 to n
for i in range(1, n + 1):
    factorial *= i

# Print the result
print(f"The factorial of {n} is: {factorial}")
