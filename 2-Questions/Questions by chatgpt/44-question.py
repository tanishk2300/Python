# Simple Inheritance
class animal:
    def sound(self):
        print("some sound")
class dog:
    def sound(self):
        print("bark")

a=animal()
a.sound()

b=dog()
b.sound()


class human:
    def sound(self):
        print("hello")

c=human()
c.sound()

