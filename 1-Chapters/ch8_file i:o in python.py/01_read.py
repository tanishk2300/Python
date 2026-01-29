#'r'(read mode)= open the file for reading. this is the default mode . if the file doesn't exist , you'll get the error .

f = open("tanishk.txt", "rt")

content =f.read()

print(content)

f.close()