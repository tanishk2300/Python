class Employee:
    company="apple"
    # those are the magic dunder 
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def __str__(self):
        return f"the name is {self.name} and the salary is {self.salary}"    
    def __repr__(self):
        return f"name: {self.name} \nsalary: {self.salary}"
    def __len__(self):
        return len(self.name)
    
        
        
e=Employee("tanishk" , 230000 ,3 ) 
print(e.name, e.salary)  
print(str(e))
print(repr(e))
print(len(e))
# there is more dunder words you have to do it first 

