import json
obj={"name":"tanishk","company":"apple","salary":"10,000,000"}
s=json.dumps(obj)#convert python object to json string.(json.dumps(obj))
print(s)
v=json.loads(s)#convert json string to python object .(json.loads(s))


# this is using of dump which help us to show the data in the file .
file=open("tannu.txt","w")
json.dump(obj,file)
file.close()


# this is using of load 

file=open("tannu.txt","r")
b=json.load(file)
print(b)
file.close()

# also this is the way we can write :-

# with open("tannu.txt", "r") as file:
#     python_data = json.load(file)

# print(python_data)  # Output: {'name': 'tanishk', 'company': 'apple', 'salary': '10,000,000'}

'''
Formatting JSON Output
You can format JSON for better readability using indentation.

'''
formatted_json = json.dumps(obj, indent=4)
print(formatted_json)