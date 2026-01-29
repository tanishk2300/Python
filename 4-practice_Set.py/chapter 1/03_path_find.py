import os 

#specify the directory path
directory_Path='.'
#get the list of files and directories
contents=os.listdir(directory_Path)
#print the contents
for item in contents:
    print(item)