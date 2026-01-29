# def convert_to_dashed_string(text: str) -> str:
#     '''
#     converts a given string to a dashed format by:
#     -removing special characters
#     -replacing spaces with dashes 
#     -converting the string to lowercase
#     '''
#     #define allowed characters: alphanumeric and space
#     allowed_chars="abcdefghijklmnopqrstuvwxyz0987654321"

#     #remove any character that is not in allowed_chars
#     cleaned_text=''. join(c for c in text if c in allowed_chars)
    
#     #split the cleaned text by spaces and hoin using dashes
#     dashed_text='-'.join(cleaned_text.split())

#     #convert to lowercase for consistancy 
#     return dashed_text.lower()

# #example usage
# input_text="hey are you good:)"
# output_text=convert_to_dashed_string(input_text)
# print(output_text)#output : "hey-are-you-good" 

# print(convert_to_dashed_string("hello,world"))

# all wrong code but you can take it an example of chatgpt 
