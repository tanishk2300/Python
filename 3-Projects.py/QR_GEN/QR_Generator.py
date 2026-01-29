import qrcode 
import os
url=input("enter your url here:")
file_name=input("enter your file name to wannt u save:")
if not(file_name.endswith(".png")):
    file_name=file_name + ".png"

f=qrcode.make(url)
f.save(file_name)
