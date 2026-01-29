#q=Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
meaning={
    "book":"पुस्तक",
    "apple":"सेब",
    "dog":"कुत्ता" ,
    "cat":"बिल्ली" ,
     "house":"घर",
   
}
# here we take the input 
word=input("apna sabde darje kare: ")
# we use here get(word) for correct and perticular ans.. and word is use to get the correct ans for it by taking the input..
meaning=meaning.get(word)

if meaning:
    print(f"{word} ka arth hindi m : {meaning}")
else:
    print("not found in our dictionary:")