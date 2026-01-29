class Employee:
    def __init__(self, salary , name , bond ):
        self.salary=salary
        self.name=name
        self.bond=bond

    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"the name of the employee (self.name).salary is (self.salary)and the bond is (self.bond) ")

e1=Employee(34000, "tanishk" ,4 )        
print(e1.get_salary())


# this is an example to get the class consept 

class ClassName:
    def __init__(self):
        # attributes like name , age --
        pass
    
    def method_name(self):
        # behavior
        pass
# here the "class" is use to define the company and ""def" - describe the object .
