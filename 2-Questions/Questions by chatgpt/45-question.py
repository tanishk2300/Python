'''6. Method Overriding

Create:

class Bank with method rateOfInterest() returning 5%

subclass SBI → returns 6%

subclass HDFC → returns 7%

Print all interest rates.'''

class bank:
    def rateOfInterest():
        return 5
class SBI:

    def rateofintrest():
        return 6
class HDFC:

    def rateofintrest():
        return 7
banks=bank()
sbi=SBI()
hdfc=HDFC()
 
print("bank of intrest", bank.rateOfInterest(),"%")
print("sbi of intrest", SBI.rateofintrest(),"%")
print("hdfc of intrest", HDFC.rateofintrest(),"%")


