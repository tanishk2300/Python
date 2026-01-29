'''

10. Encapsulation – Private Variables

Create a class Account with:

private variable balance

deposit()

withdraw()

getBalance()

Balance should not be accessed directly.

'''
class account:
    def __init__(self,balance=0):
        self.__balance=balance

    def deposit(self,amount):
        if amount>=self.__balance:
            self.__balance+=amount
            print("your amount is deposited ",self.__balance)
        else:
            print("invalid amount")

    def withdraw(self,amount):
        if amount>=0:
            self.__balance-=amount
            print("succesful ,remaining balance:",{self.__balance})
        else: 
            print("rejected ")

    def getBalance(self):
        print("total balance=",self.__balance)
    

a=account(0)
for i in range (1,3):
    d=input("deposit(a)/withdraw(b)")
    if d=="a":
        dep_money=int(input("enter amount to deposit :"))
        a.deposit(dep_money)
    
    elif d=="b":
        wid_money =int(input("enter amount to withdraw :"))
        a.withdraw(wid_money)
    else:
        print("choose again ")


a.getBalance()




        



