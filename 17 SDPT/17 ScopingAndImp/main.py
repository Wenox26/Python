# VAR SCOPING

#GLOBAL VAR
y = "World"



#LOCAL VAR
# def sayHello():
#     x = "Hello"
#     print(x + y)
#     print(y)
    
# sayHello()


#PARAMETER VAR
# def say(word):
#     print(word)
    

#GLOBAL KEYWORD
# def say():
#     global y #GOBAL VAR
#     y = "Hello"
#     print(y)

# say()
# print(y)

#IMPORT KEYWORD
# import constants as a
# import arithmetic as b
# import object as c

# # print(constants.pi)

# pOne = object.Student("Owen", "BSIT")

# pOne.introduce()



#"AS" KEYWORD
# a.pi
# b.add
# c.Student


#FROM KEYWORD 
# from arithmetic import add as a
# from object import Student 


# print(a(2,4))

#IMPORTING FROM ANOTHER FILE
import sdpt.arithmetic

sdpt.arithmetic.add()



