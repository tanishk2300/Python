#virtual enviroment - a virtual enviroment is a self-contained directory that contains its own pthon interpreteer and liberaries . this mean that libraries install in one virtual enviroment won't interfere with liberaries in another .
# firstly we install = pip install pandas
# second we install = pip install moviepy
# v1 - pakage 1 (pandas)
# v2 - pakage 2 (numpy)
# v3 - pakage 3 (moviepy)
#there is a globale virtual machine which help us to make our project run smooth and it make it latest updated .
# suppose we need the other vesion of the package for my project than the virtual enviroment help us in this.
# now we install a vertual enviroment here by - pip install virtualenv
# now we create a new virtual enviromet - python -m venv env1(name of the virtual enviroment here i use env1)
#downlode powershell if it's not .
# now activate env1 use - source env1/bin/activate
# pip list -show the pakeges which u downlode in 
# then use - pip install pandas
# then use - pip install requests 
# install - pip scipy 
# and then u see by pip list is scipy install or not 
# we can upgrade perticular package by - pip install--upgrade reques(name of package)
# for uninstall use - pip uninstall requests 
#i can create a file for user of my project and i wanna to tell my user that the newer version of packege by file requirement.txt use for better preform by single file is called requirement 
# pip freeze - is use to see the packege and the version of it .
# here we wanna give the update of latest package to user of my project so i will use - pip freeze > requirement.txt 
# now you can see the file requirement.txt on your left side .
#after this all now we create a new env , env2 and activate it as before 
#now if i wannt to install whole packege pf requirement.txt in one click so , use - pip install -r ./requirement.txt
# now they being install , done.
#now we wanna be use the ' moviepy ' to buit projects but in this enviroment there is no moviepy install it gives error . but, we install before it globely so why , becouse its a diff env... (env2) so now install it first ,



# python3 -m venv my_env  # Creates a virtual environment named "my_env" use it in terminal 
# source my_env/bin/activate
# deactivate
'''
pip install requests  # Installs the "requests" library
pip install numpy==1.20.0 # Installs a specific version
Once activated, you'll see the virtual environment's name in your terminal prompt (e.g., (my_env)).
'''