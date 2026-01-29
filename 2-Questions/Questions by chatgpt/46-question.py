'''7. Multilevel Inheritance

Person → Employee → Manager
Each should have its own method.
Create an object of Manager and call all methods.

'''

class person:
    def personinfo(self):
        print(" i am a person ")
class employ(person):
    def employinfo(self):
        print("i am a employ as a person ")
class manager(employ):
    def managerinfo(self):
        print(" i'm a manager ")
m=manager()

m.personinfo()
m.employinfo()
m.managerinfo()






