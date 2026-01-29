# here we start the getter and setter 
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @property 
    def first_name(self):
        l=self.name.split(" ")
        return l[0]
    @first_name.setter
    def set_first_name(self,first):
        l=self.name.split(" ")
        new_name=f"{first} {l[1]}"
        self.name=new_name

e=Employee("love benecar ", 2300)

#print(e.first_name())# it help to print the name accd... to the command .
print(e.first_name)
#e.first_name = "love"
print(e.name)# help to get the salary 


