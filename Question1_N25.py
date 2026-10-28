# Parta(i)
class Bird:
    def __init__(self,pSpecies,pDistancePerHour): 
        self.__Species= pSpecies                     # STRING
        self.__DistancePerHour = pDistancePerHour    # REAL
        self.__XPosition = 500.0                     # REAL
        self.__YPosition = 500.0                     # REAL
    # Parta(ii)
    def GetSpecies(self):
        return self.__Species

    #part a(iii)
    def GetPostion(self):
        Postion = "X = " + str(self.__XPosition) + " Y = " + str(self.__YPosition)
        return Postion

    # part a (iv)
    def move(self, Direction,Minutes):
        Distance = (self.__DistancePerHour/60) * Minutes
        if Direction == 'N':
            self.__YPosition = self.__YPosition + Distance
        elif Direction == 'S':
            self.__YPosition = self.__YPosition - Distance
        elif Direction == 'E':
            self.__XPosition = self.__XPosition + Distance
        elif Direction == 'W':
            self.__XPosition = self.__XPosition -  Distance
        else:
            print("Enter the Correct Character, Please!")
        return self.__XPosition, self.__YPosition



# Part b
#...........................Main Program..................................
Bird1 = Bird('Cockatiel',71.0)
Bird2 = Bird('Mascaw',56.0)

# Part C (i)
print("Type of Specie",Bird1.GetSpecies(),"Current X Positon and Current Y Position",Bird1.GetPostion())
print("Type of Specie",Bird2.GetSpecies(),"Current X Positon and Current Y Position",Bird2.GetPostion())
Choice = input("Enter One of the birds to move,Bird1 or Bird2:")
Direction = input("Enter the direction the bird has been travelling as 'N','S','W', or 'E':")
Minutes = int(input("Enter the time the bird has been travelling to the nearest minute:"))
if Choice == "Bird1":
    Choice = Bird1
elif Choice == "Bird2":
    Choice= Bird2
else:
    print("Incorrect Input ")

Choice.move(Direction,Minutes)
print(Choice.GetPostion())


