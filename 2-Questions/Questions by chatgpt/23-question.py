'''Q-Take the string "  i love python programming  " and:

        1.Remove extra spaces from both ends
        2.Convert it to title case
        3.Count how many times "o" appears
        4.Convert it to large case '''

string=" i love python programming  "

# 1.Remove extra spaces from both ends
clean_string=string.strip()
print(clean_string) # this help the string to remove the extra space from the last and first of the stsring .

# 2.Convert it to title case
string2="I LOVE PYTHON "
string2_lower=string2.lower()
print(string2_lower)# this help to make the string lower case .

# 3.Count how many times "o" appears
string_count=string.count("o")
print(string_count) #this help to count the thing in the string 

# 4.Convert it to large case
string_upper=string.upper()
print(string_upper)