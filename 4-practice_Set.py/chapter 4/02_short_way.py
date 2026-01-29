#q=Write a program to accept marks of 6 students and display them in a sorted manner.
 
def get_marks():
    marks=[]
    for i in range(6):
        mark=input("enter the number each student gain: ")
        marks.append(mark)
    return marks
list=get_marks()
print("list of the marks ",list)