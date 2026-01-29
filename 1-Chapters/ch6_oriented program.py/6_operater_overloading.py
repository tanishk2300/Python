class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def sum(self, p):
        return point((self.x + p.x),(self.y + p.y))
    
    
    def print_point(self): # here def is defination  and print point function is use to print the result 
        return (f"X is {self.x} and Y is {self.y}") 
    def __add__(self,p):# it work when we use the p1+p2 .
        return point((self.x + p.x) , (self.y + p.y))
    

p1=point(3, 2)
p2=point(6, 3)
# here the p=p1.sum(p2) use to sum the x,y point .
#p=p1.sum(p2) #returns a new point which is sum of p1 and p2 .
p=p1+p2 # it cant work when we dont write the add function . we overloaded the + operator by writing __add__ function .
print(p.print_point())#help to print 
