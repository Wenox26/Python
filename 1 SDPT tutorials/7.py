# FOR LOOP
#CTRL + / to comment
# fruits = ["Apple", "Banana", "Orange"]

# #for every x in fruits
# for x in fruits:
#     print (x)
    
#else in fruit

# fruits = ["Apple", "Banana", "Orange"]

# #for every x in fruits
# # for x in fruits:
# #     print (x)
# # else:
# #     print ("No more fruits")

# for x in fruits:
#     print (x)
#     if x == "Banana":
#         break
    
    
# numbers = [1,2,3,4,5,6,7,8,9,10]

# for number in numbers:
#     if number % 2 == 0:
#         print ("Even number: " + str(number)) 
#     else:
#         print("Odd numbers: " + str(number))

# range
# for x in range(10):
#     print ("Hello world!")

#CHALLENGE

username = ["Jhon", "Alenere",  "David"]
password = ["abc123", "123abc", "hahatdog"]

currUsername = input("Username: ")
currPassword = input("Password: ")

for x in range(len(username)):
    if currUsername == username[x] and currPassword == password:
        print ("Welcome " + username[x])
        break
else:
    print("Invalid input")
