class Employee:
    company="asus"
    def __init__(self, salary , name , bond,company):
        self.salary=salary
        self.name=name
        self.bond=bond
        self.company=company


    def get_salary(Self):
        return Self.salary
    def get_info(self):
        print("the name of the employee is {Self.name}. salary is {self.salary}. the bond is for {self.bond} year.")
    

e1=Employee(3400,"john",3 , "tesla")
print(e1.company)     
print(Employee.company) #this will always print the class attribute .

#object introspection 
#the way to find all the method that a perticular object in python has

print(dir(e1)) # this help to print all the method on this 