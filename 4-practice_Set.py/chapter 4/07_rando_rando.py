numbers=[]# use to store the number 

def get_number():
    for i in range(8):
        num=int(input(f"enter the numbers {i+1};"))
        numbers.append(num)
    return num

list=get_number()
print("\n unique number is here: ")

unique_number=set(numbers)# use to take the unique number and take from the set number 

for numbers in unique_number:# take the number from the upper case 
    print(numbers)
