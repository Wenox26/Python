#INHERITANCE

#Parent class and Child class
#PARENT CLASS
# class Person:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName
        
#     def introduction(self):
#         print ("Hi I am " + self.firstName,self.lastName)
        
# #CHILD CLASS
# class Student(Person):
#     pass

# pOne = Person ("Owen", "Jeru")
# pOne.introduction()

# pTwo = Student("WenWen", "Jerusalem")
# pTwo.introduction()

#OVERRIDING CONSTRUCTOR
# class Person:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName
        
#     def introduction(self):
#         print ("Hi I am " + self.firstName,self.lastName)
        
# #CHILD CLASS
# class Student(Person):
#     def __init__(self,firstName,lastName,sectionYear):
#         super().__init__(firstName, lastName)
#         self.sectionYear = sectionYear
        
# sOne = Student("Owen", "Jerusalem", "HUMSS 12- KRYPTON")

#OVERRIDING FUNCTION

#PARENT CLASS
class Person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def introduction(self):
        print ("Hi I am " + self.firstName,self.lastName)
        
#CHILD CLASS
class Student(Person):
    def __init__(self,firstName,lastName,sectionYear):
        super().__init__(firstName, lastName)
        self.sectionYear = sectionYear
    def introduction(self):
        print("Hi I am " + self.firstName, self.lastName + " FROM " + self.sectionYear)
        
pOne = Person("Wenwen", "Jerusalem")
sOne = Student("Owen", "Jerusalem", "HUMSS 12- KRYPTON")
pTwo = Person("OWEN", "JERUSALEM")

pOne.introduction()
sOne.introduction()
pTwo.introduction()
