# # Create an empty dictionary
# fav_languages = {}

# # Taking input from 4 friends
# fav_languages[input("Enter your name: ")] = input("Enter your favorite language: ")
# fav_languages[input("Enter your name: ")] = input("Enter your favorite language: ")
# fav_languages[input("Enter your name: ")] = input("Enter your favorite language: ")
# fav_languages[input("Enter your name: ")] = input("Enter your favorite language: ")

# # Print the final dictionary
# print("\nFavorite Languages:")
# print(fav_languages)
dict={}

for i in range(4):
        name=input(f"Enter your name{i+1} : ")
        language=input(f"{name} your fav. language: ")
        dict[name]=language
        
print("\n fav. language of friends: ")
for name, language in dict.items():
    print(f"{language} of {name} ")



    



