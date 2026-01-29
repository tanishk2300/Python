class Animal: #parent class (superclass)
    location="Australia"
    def __init__(self,name):
        self.name=name
    def speak(Self):
        print("speaking now....")

class dog(Animal): # this is how inheritance is done in python 
    def speak(self):
        super().speak() # here super call the speak function from the upper parent class function .
        print("woof!")


#a=Animal("dog")
#a.speak()
d=dog("bruno")
d.speak()
#print(d.location)

        