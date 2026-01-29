#'w' (write mode)= open the file for writing . if the file exists ,its contents will be overwritten . if the file doesn't exist, a new file will be created.
# write to a file called john doe.txt 
#it should contain data about john doe .
#

f = open("john doe.txt", "w")

string= '''
hey this is john doe and i am write a phase regard my life...
'''
f.write(string)
f.close()
# now the file is created and the string is writen in it on your left side of file .