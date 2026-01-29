'''9. Operator Overloading

Create a class Point where:

Overload + to add two points (x1+x2, y1+y2)'''

class points:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def  sum(self,p):
        return points((self.x+p.x),(self.y+p.y))

    def  point(self):
       print(f"x is {self.x} and y is {self.y}")
    def __str__(self): # this is the string function 
        return f"({self.x},{self.y})"
 

p1=points(3,5)
p2=points(9,5)

f=p1.sum(p2)
f.point()

print(p1) # here you get somthing like " <__main__.points object at 0x10232ea50>" for get correct one we use "__str__" function  