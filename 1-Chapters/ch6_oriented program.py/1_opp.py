# here the object oriented programming is like :-
'''let u have a train form and that form ask u for your class and 
your gender etc. and give u a info about the train the the person and that info is called objects .
let the class is car and you dont know which compney the car belongs , if we give the name like BMW,Mercedes,Audi. 
those are the objects. 

# class is like a form and if we fill it the filling is called object .

#why bother with oop?
oop offers several advantages;
* organization-your code becomes more structuered and easier to navigate large projects become much more manageable.
* reusability-you can use the same object "blueprints" (classes) multiple tunes saving you from writing the same code over and over .
* easier debugging-when something goes wrong , it's often easier to pinpoint the problem within a specific, self-contained object.
* real-world modeling-oop allows you to represent real-world things and their relationships in a natural way.

You said:
the four pillor of oop?

ChatGPT said:
The four pillars of Object-Oriented Programming (OOP) are:

1.Encapsulation:- (this protect the data from being accidentally changed or misused from outside the object. it controle access)

 Wrapping data (attributes) and methods (functions) that operate on the data into a single unit called a class.
 It restricts direct access to some of the object's components, which means the internal representation of an object is hidden from the outside.

2.Abstraction:- (it hide the complex info and show only essential info )

Hiding complex implementation details and showing only the essential features of the object.
It helps in reducing complexity by exposing only what is necessary.

3.Inheritance:- (this promotes codee reuse and reduces redundancy , its like a modification in code )

Mechanism where one class (child or subclass) inherits properties and behavior (methods) from another class (parent or superclass).
It promotes code reuse and establishes a relationship between classes.

4.Polymorphism:-(example - a 'Dog' and 'Cat' might have a method [make_sound()] . the dog will bark , and the cat will meow - same method name ,, different behavior .)

Ability of different classes to be treated as instances of the same class through a common interface.
It allows one interface to be used for a general class of actions, with specific behavior determined by the exact nature of the situation (method overriding or overloading)
'''


#here 
class animal:
    def __init__(self, name):
        self.name=name
def makesound(self):  
    pass
class Dog(animal):
    def makesound(self):
        return f"{self.name} says: boww!" 
    
class Cat(animal):
    def makesound(self):
        return f"{self.name} says: meow! "
        
#example usage
dog=Dog("buddy")        
cat=Cat("whiskers")

print(dog.makesound())
print(cat.makesound())

