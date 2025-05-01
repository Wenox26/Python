#DICTIONARY---------------------------------------------------------------

#1

studentOne = {
    "name": "OWEN", 
    "course": "BSIT", 
    "age": 17
}

studentTwo = {
    "name": "WENOX",
    "course": "BSCS",
    "age": 18
}

studentOne["age"] = 18
studentOne["gender"] = "Male"
#studentOne.pop("age")
#studentOne.popitem()
#studentOne.clear()
#print (studentOne.get("age"))
#print (len(studentOne))

#studentThree = studentOne.copy()

#print (studentOne.values())

#LIST DICT

studentOne = {
    "name": "OWEN", 
    "course": "BSIT", 
    "age": 17
}

studentTwo = {
    "name": "WENOX",
    "course": "BSCS",
    "age": 18
}

students = [studentOne,studentTwo]

#print (students)

#Accessing specified data
#ex

#print (students[0].get("name"))
#print (students[1].get("name"))

#NESTED DICT

studentOneAttributes = {
    "height": 163,
    "weight": 52,
    "skin": "White"
}

studentOne = {
    "name": "OWEN", 
    "course": "BSIT", 
    "age": 17,
    "physical": studentOneAttributes
}

studentTwo = {
    "name": "WENOX",
    "course": "BSCS",
    "age": 18
}

print (studentOne.get("physical"))

