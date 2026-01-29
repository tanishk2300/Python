name="tanishk jangid " #string is immutable 
#name[0] = 'n'# you cannot do this this 
a= len(name)#use to measuse the length of the string 
print(a)
# answar is 7
print(name.upper())#convert into upper case 
print(name.lower())
print(name.capitalize())
print(name.title())

#here we use the strips 
text=" hallow world "
print(text.strip()) #it helps to ending the new line ,output="hellow world"
print(text.lstrip()) # it ending the left side ,output="hellow world"
print(text.rstrip()) #it ending the right side ,output =" hellow world "

#here,
text="python is fun and fun and fun " 
print(text.replace("fun","awesome")) #it helps us to replace the word 
print(text.find("is")) #it helps us to find where word is present 


#now,
text="apple,bannana,pineapple"
print(text.split(","))  #here it helps us to split the tupple
print(",".join(["apples","bannana","pineapple"]))  # here it use to join the tupple 

#now,
text="python1234"
print(text.isalpha())#it tells us if it contain only alphabet it will be true 
print(text.isdigit())#it tells us if it contain only digit it will be true 
print(text.isalnum())#isalnum tells us if it contain alphabet and number its true 
print(text.isspace())#isspace tells us this character has only wild space characters 
