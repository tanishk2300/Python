#'a'(append mode )= opens the file for appending data will be added to the end of the file . if the file doesn't exist a new file will be created.
f=open("john doe.txt","a")# if we use 'w' here the data of the whole file was wiped out .
string='''
hey i am edit something here..
'''
f.write(string)
f.close()
# now the new content was printed in it.
