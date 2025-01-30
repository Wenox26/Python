#ARGUMENTS

# ABITRARY
# def sayHello (*names):
#     for name in names:
#         print(name)
        
# sayHello("Owen", "Wenox", "Chawchaw", "Papi")


# def printFamily (*names):
#     for name in names:
#         print ("Hello" + " " + name)
        
# printFamily ("Owen", "Wenox", "Chawchaw", "Papi")


    
#KEYWORD ARGUMENTS
# def printFamily (*firstNames, lastName):
#     for name in firstNames:
#         print (name + " " + lastName)
        
# printFamily ("Owen", "Wenox", "Chawchaw", "Papi", lastName= "Bogart")
     
#ARBITRARY KEYWORD ARGUMENTS   
# def printStudent (**student):
#     print(student["name"])
#     print(student["lastName"])
#     print(student["age"])
#     print(student["course"])
    
    
# printStudent (name= "Owen", lastName= "Jeru", age= "17", course= "BSIT")

#challenge

# def infiniteNumbers (*numbers):
#     sum = 0
#     for number in numbers:
#         sum += number
#     return sum

# print(infiniteNumbers (1,2,3,3,4,34,34,3,54,4,6,5))