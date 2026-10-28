# Hello Wordl How are you.......
# Part a
import random
NumberList = random.sample(range(1,101),20)

# part b


def PrintArray(NumberList):
    print(" ".join(str(Number) for Number in NumberList))



# part C
def BubbleSort(NumberList):
    Length = len(NumberList)
    while Length <= len(NumberList) and Length >=1:
        for i in range(len(NumberList)-1):
         if NumberList[i] > NumberList[i + 1]:
            Temp= NumberList[i]
            NumberList[i] = NumberList[i+1]
            NumberList[i+1] = Temp
         else:
            break
    return NumberList



#......................Main program................................
# Part d(i)
PrintArray(NumberList)
NumberList = BubbleSort(NumberList)
print("Sorted")
PrintArray(NumberList)


# Part (e)
def RecursiveBinarySearch(NumberList,Min,Max,Target):
    Index = 0
    low = Min
    upper = Max
    Mid = (low + upper)//2
    while low >= upper and Index < len(NumberList):
        for Index in range(0,len(NumberList)):
                if NumberList[Mid] != Target:
                    if NumberList[Mid]> Target:
                        low = Mid +1
                    else:
                        upper = Mid - 1
                    return -1 
                else:
                    return Index

#..................................Main Program......................
User = int(input("Please enter an integer as a target:"))
Check = RecursiveBinarySearch(NumberList,0,20,User)
if not Check:
    print("Not found")
else:
    print("Found at Position",Check)