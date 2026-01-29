class Employee:
    company="apple"
    def __init__(self , name , salary ):
        self.name=name
        self.salary=salary

    #instance method (default)
    def print_info(self):
        info=f"The name is {self.name} and the salary is {self.salary}."
        print(info)

        
    #static method 
    @staticmethod# it work's when we write the "@staticmethod" otherwise it cant able to work it is only use for adding and something like it 
    def sum(a,b):
        return a+b
    

    #classmethod 
    @classmethod
    def print_company(cls):
        print(cls.company)
    @classmethod
    def change_company(cls, new_company):
        cls.company=new_company


    


e1=Employee("tanishk" , 10000000)
e2=Employee("jack",200)
#print(e1.company)
#print(e2.salary,e2.name)
#print(e1.name,e1.salary)
#e1.print_info()
#print(e2.sum(2, 3))
print(Employee.company)#here employee is the class.
e1.change_company("acer")
print(Employee.company)