# While Loop
 
# age = 17

# while age < 18:
#     print ("Still young: " + str(age))
#     age = age + 1
# else:
#     print ("Legal Age: " + str(age))

# studentID = [2000123,2000124,2000125,2000126,2000127]
# i = 0

# while i < len(studentID):
#     print (studentID [i])
#     i = i + 1

#BREAK
# while True:
#     print ("Hello World")
#     break

# print ("Crush ka ba ng Crush Mo?")

# while True:
#     answer = input("Answer: ")
#     if answer == "hinde":
#         print ("CORRECT")
#         break
#     else:
#          print ("Mali ka diyan kapatid!")

# numbers = [1,2,3,4,5,6,7,8,9,10]
# i = 0 

# while i < len(numbers):
#     if(numbers[i]) % 2 == 0:              # % = Modulus
#         print ("Even Number: " + str (numbers[i]))
#     else:
#         print ("Odd Numbers: " + str(numbers[i]))
#     i = i+1

chances = 3
correctAnswer= 150

while chances > 0:
    answer = int(input("100 + 50 = "))
    if answer == correctAnswer:
        print ('Very Good!')
        break
    else:
       chances = chances - 1
else:
    print ('You Lose!')
    
    