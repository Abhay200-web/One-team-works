class Students:
    college="MGM" # this is a class attribute
    course="Computer science Engineering "
    semester="Semester 8"

    def __init__(self,n,r,h): # self is the reference of the object
        self.name=n
        self.age=r
        self.height=h

stud1=Students("abhay",23,157)  #stud1 is an object in class Student
stud2=Students("abhi",33,160)
print(stud1.name,stud1.age,stud1.height)
print(stud2.name,stud2.age,stud2.height)
print(Students.college)  # this is a clas attribute it cn be called by the ---->"classname.attributename"
print(Students.course)
print(Students.semester)











