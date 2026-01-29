#python's os module provide function or interacting with the operating system such as working with directories and fules the shutil module offers higher-lefvel file operations.

# os module: allows you to interact with the operating system manage files and directories and perform tasks like creating , deleting and renaming files . 
# it also provide access to system information such as enviroment variables and current working directory.

#shutil module: provides higher-level file operations like coping , moving ,and deleting file and directories . 
# it also includes functionality for archiving file and direvtories into formats like ZIP.

import os 
a=os.listdir("dir")
print(a)
print(os.getcwd())
print(os.path.exists("dir"))# it help to give the eexistance of file path is true or false .
# os.remove("sample.txt")#it remove the file which is exist , from outside of the "dir" it cant remove the directries .
os.rmdir("dir")# it can only remove empty directries .
