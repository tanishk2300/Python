#there is two type of modules in pyrhon :
#-built in module 
#-external modules 
# list of all module -   https://docs.python.org/3/py-modindex.html
import math #import is use to import a module 
print(math.sqrt(16))#the dot after math it mean i want to use math as a fuction

import mymodule
mymodule.hello()

import requests
r=requests.get("https://www.google.com")
print(r.text)
