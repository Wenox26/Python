#COLECTION OF OBJECTS 

# class Person:
#     def __init__(self,name):
#         self.name = name
#         print (self.name + " Created")
        
        
# name = input ("Enter name: ")
# pOne = Person(name)

#STORE OBJECT IN COLLECTION
# class Person:
#     def __init__(self,name):
#         self.name = name
    
#     def Introduce(self):
#         print("We are " + self.name)
        
# pOne = Person("JM")
# pTwo = Person("Nica")
# pThree = Person("Nashnash")

# listOfHumans = [pOne,pTwo,pThree] 
# listOfHumans.Introduce()

#USING LOOPS TO READ COLLECTIONS
# class Person:
#     def __init__(self,name):
#         self.name = name
    
# pOne = Person("JM")
# pTwo = Person("Nica")
# pThree = Person("Nashnash")
# p4 = Person("Joy")

# listOfHumans = [pOne,pTwo,pThree,p4]

# for person in listOfHumans:
#     print(person.name)

#USING LOOP TO WRITE IN COLLECTIONS
# class Person:
#     def __init__(self,name):
#         self.name = name
        
#     def Introduce(self):
#         print("Hi I am " + self.name + "a certified gay")
        

# listOfHumans = []

# for i in range(3):
#     name = input("Enter Name: ")
#     p = Person(name)
#     listOfHumans.append(p)
    
# for person in listOfHumans:
#     print(person.name)

#CHALLENGE: STUDENT REGISTRATION 
# class Student:
#     def __init__(self,name,course,year,section):
#         self.name = name
#         self.course = course
#         self.year = year
#         self.section = section

# listOfStudents = []

# for i in range(0):
#     s = Student(name,course,year,section)
#     name = input("Enter Name: ")
#     course = input("Enter Course: ")
#     year = input("Enter Year: ")
#     section = input("Enter Section: ")
#     listOfStudents.append(s)

# for student in listOfStudents:
#     print(student.s)
#----------------------------------------------------------------------------
class Student:
    def __init__(self,name,course,year,section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section
        
    def introduce(self):
        print("Name " + self.name)
        print("Course " + self.course)
        print("Year " + self.year)
        print("Section " + self.section)
        
listOfStudents = []

while True:
    print()
    name = input("Name   : ")
    course = input("Course : ")
    year = input("Year   : ")
    section = input("Section: ")
    s = Student(name,course,year,section)
    listOfStudents.append(s)
    print()
    
    choice = input("Create another Student info? [Y/Any char] : ")
    
    if choice == 'Y' or choice == 'y': 
        pass
    else: 
        break
    
