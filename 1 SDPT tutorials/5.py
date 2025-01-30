#IF, ELSE, ELIF WHILE LOOP

#age = 1

#while age < 18:
    #print("Still young:" + str(age))
    #age = age + 1
#else:
 #   print("Your'e Old: " + str(age))
 
#studentID = [2000123, 2000124, 2000125, 2000126]

#i = 1

##while i < 3:
    #print (studentID)
    
#if else statement
#password = input("Enter password: ")

#if password == "QWERTY26":
#    print ("Access granted!")
#else:
#    print ("Access denied.")

# IF-ELIF-ELSE Statement

# age = int(input("Enter age: "))

# if age >= 18:
#     print ("Legal age")
# elif age == (12,13,14,15,16,17):
#     print ("Teenager")
# elif age <= 11:
#     print ("Kid")
# else:
#     print ("Too young") 


#OR, AND statements
#example

# hasRuler = True
# hasMeterstick = False

# if hasRuler or hasMeterstick:
#     print ('Very good!')
# else:
#     print ('your a bad kid')

# hasRuler = True
# hasMeterstick = True

# if hasRuler and hasMeterstick:
#     print ('Very Good!')
# else:
#     print ('Your a bad kid!')


gradeOne = float(input("Math: "))
gradeTwo = float(input("English: "))
gradeThree = float(input("Science: "))

average = (gradeOne + gradeTwo + gradeThree) / 3

print ("AVERAGE:" + str(average))

if average > 100 or average <= 50:
    print ("Invalid Grade.")
elif average >= 98:
    print ("With Highest Honors")
elif average >= 95:
    print ("With High Honors")
elif average >= 90:
    print ("With Honors")
elif average >= 75:
    print ("Passed")
else:
    print ("Failed")
