# create a list containing the table of 5 
#it use to edit in this function and write any function in it .

table=[]

for i in range(1,11):
    table.append(5*i)

print(table)    

# other method to print the table 
#this is only use for table and dont want to edit or change into it .
table=[5*i for i in range(1,11)]
print(table)
