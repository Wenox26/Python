#OOP OBJECT FUNCTIONS
# class Animal:
#     def __init__(self,type,voice,size):
#         self.type = type
#         self.voice = voice
#         self.size = size
        
#     def speak(self):
#         print(self.voice)
        
#     def introduceSelf(self):
#         print("I am a " + self.type)
        
#     def sizeAnimal(self):
#         print(self.size)

# aOne = Animal("Dog", "Aw-aw", "Big")
# aTwo = Animal("Cat", "Meow", "Small")

# aOne.speak()
# aOne.introduceSelf()
# aOne.sizeAnimal()
# aTwo.speak()
# aTwo.introduceSelf()
# aTwo.sizeAnimal()

#CHALLENGE
class User:
    def __init__(self, firstName, lastName, likesCount, friendsName):
        self.firstName = firstName
        self.lastName = lastName
        self.likesCount = likesCount
        self.friendsName = friendsName
        print("User Created: " + self.firstName,self.lastName)
    
    def nameUser(self):
        print("Hi I'm " + self.firstName, self.lastName)
    
    def socialMlikes(self):
        print(self.likesCount)
    
    def friends(self):
        print(self.friendsName)
        
userOne = User("Owen", "Jeru", "1M Likes", 
        ["Bogart", "Jayat", "Ariana Grande", "Yskaela FUjimoto"])
# userTwo = User("Wenwen", "Jerusalem", "100M Likes", 
#         ["Andrew Tate", "Dwayne Johnson", "Tom Cruise", "Charles Darwin"])

# #USER ONE
userOne.nameUser()
userOne.socialMlikes()
userOne.friends()


# #USER TWO
# userTwo.nameUser()
# userTwo.socialMlikes()
# userTwo.friends()
