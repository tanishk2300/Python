import requests 
#using api to take the accese their data .
r = requests.get('https://api.github.com/users/codewithharry')# it is a request to take permisson form the module owner.. 

with open("codewithharry.txt","w") as f:
    f.write(r.text)
    # this help to screape the data of your project and site , mean if the site and anything crash and give error it will save your code by it , its your saver of your project .