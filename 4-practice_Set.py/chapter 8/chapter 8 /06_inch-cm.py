#q=Write a python function which converts inches to cms.
def get_cm(inch):
    cm=inch*2.54
    return cm
a= int(input("enter the inch: "))
print(F"{get_cm(a)} cm in {a}inch")
