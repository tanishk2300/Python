# q=Write a python function to remove a given word from a list ad strip it at the same time.
def remove_and_strip(word_list, remove_word):
    # Strip both the list items and the remove_word before comparison
    return [item.strip() for item in word_list if item.strip() != remove_word.strip()]

my_list = ("banana", "apple", "mango", "tometo")
word_to_remove = "banana"

result = remove_and_strip(my_list, word_to_remove)
print(result)
# def remove_and_strip(word_list, remove_word):
#     # Use list comprehension to strip each element and filter out the remove_word
#     return [item.strip() for item in word_list if item.strip() != remove_word]

# # Example usage
# my_list = ["  apple  ", "banana", "  mango  ", "banana  ", "  grape"]
# word_to_remove = "banana"

# result = remove_and_strip(my_list, word_to_remove)
# print(result)  # Output: ['apple', 'mango', 'grape']
