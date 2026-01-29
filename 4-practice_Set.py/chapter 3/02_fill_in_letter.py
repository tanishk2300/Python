#q=Write a program to fill in a letter template given below with name and date
name=input("enter the name=")
date=input("enter the date=")

letter='''
dear <|NAME|>
you are selected!
<|DATE|>
'''

letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)

print(letter)