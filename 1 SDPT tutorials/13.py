#OOP CONSTRUCTORS
#Puts values in attributes

#initialize function
#__init__

# class Character:
#     def __init__(self):
#         print ("Character Created")
        
# charOne = Character()
# charTwo = Character()
# charThree = Character()

#SELF PARAMETER (CONSTRUCTOR)
class Character:
    def __init__(self,name,hp,mp,atk,lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.lvl = lvl
        print("Created " + self.name)

charOne = Character("Owen", 100, 50, 30, 1) 
charTwo = Character("Wenwen", 200, 34, 5, 34)
charThree = Character("Miya", 100, 50, 100, 1)


