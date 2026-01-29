# q=Write a python program using function to convert Celsius to Fahrenheit.
#function to conver to celsius to fahrenheit 
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
#take input from the user 
c=float(input("enter the temp. in celsius: "))
#call the function and display result
f=celsius_to_fahrenheit(c)
print(f'{c}°C is equal to {f}°F')

