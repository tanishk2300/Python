'''8. Create a Book class

Include:

title, author, price

discount method: returns price after discount %

✅ Advanced OOP Coding Questions'''

class book:
    def __init__(self, title ,auther,prize):
        self.title=title
        self.auther=auther
        self.prize=prize
    def discount(self,percent):
        discount_prize=self.prize*(percent/100)
        final_prize=self.prize-discount_prize
        return final_prize
    

a=book("the advanture","tanishk",600)
print("discounted price",a.discount( 20))#"this is how much discout need like 20% , so i write 20 !



    




