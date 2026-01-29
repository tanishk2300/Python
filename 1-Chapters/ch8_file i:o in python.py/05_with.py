# f = open("tanishk.txt", "rt")
# content =f.read()
# print(content)
# f.close()

#rether this we can do like if we dont want to use 'f.close()' to close the file we use 'with'

with open("tanishk.txt","r") as f: # context manegar.
    content=f.read()
    print(content) 
# this is the way ..
# no need to write f.close() becouse file is already close by default when using with synax 