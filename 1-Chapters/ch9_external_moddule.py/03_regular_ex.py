#--Learn how to use regular expressions in Python with the re module.
#This allows you to search, match, and manipulate strings based on 
#patterns, making tasks like validation,
#text parsing, and data extraction more efficient.
import re
text="The quick brown fox jumps over the lazy dog."
## search for a pattern 
# match=re.search("brown",text)
# print(match)
# if match:
#     print("match found!")
#     print("start index:",match.start())
#     print("End index:",match.end())

# #find all occurrences of a pattern
# match=re.findall("the",text,re.IGNORECASE)#case insensitive search 
# print("match:",match)
new_text=re.sub("fox","cat",text)
print("New text:",new_text)