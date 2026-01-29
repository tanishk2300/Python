# class : class is a blueprint or a template, eg- form for an exam that contains name, age,electives,father's name etc.

# object: specific instance created from the template (class.) eg. form which contains the data for john doe

''' 
make you easy to get the class and object -
let you have an car , which is consider as a class 
and the company a specific , by whom you get that which car 
it is the car describe by the company like "BMW" it is identiti for car 
like that "object" is use to give a specility of that thing
object has its own unique set of data it's like the actual house built from the architecture plan.
  '''

class employee:
    company="HP"

    def get_salary(self): #self refrences which is talk about , self is imp... here becouse self is a way to reference the object of the class which is being created   
        return 43000
    
e=employee()   # an object of class employe is created here  
print(e.get_salary())# employee's get salary method is called 



e2=employee()
print(e2.get_salary())
print(e2.company)
# ___________________________________________example of class____________________

class Dog:  # We define a class called "Dog"
    species = "Canis familiaris" # A class attribute (shared by all Dogs)

    def __init__(self, name, breed):  # The constructor (explained later)
        self.name = name     # An instance attribute to store the dog's name
        self.breed = breed   # An instance attribute to store the dog's breed

    def bark(self):          # A method (an action the dog can do)
        print(f"{self.name} says Woof!")

# Now, let's create some Dog objects:
my_dog = Dog("Buddy", "Golden Retriever")  # Creating an object called my_dog
another_dog = Dog("Lucy", "Labrador")     # Creating another object

# We can access their attributes:
print(my_dog.name)       # Output: Buddy
print(another_dog.breed)  # Output: Labrador

# And make them perform actions:
my_dog.bark()            # Output: Buddy says Woof!
print(Dog.species)       # Output: Canis familiaris