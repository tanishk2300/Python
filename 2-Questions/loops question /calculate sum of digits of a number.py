num =int(input("enter a number.."))
sum_of_digit=0
while num > 0:
    digit=num%10
    sum_of_digit+=digit
    num//=10
print("sum of digit",sum_of_digit)
