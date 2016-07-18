from Myro import *
myList=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#print(myList)

mySecondList=[0, 0, 0, 0, 0]
#print(len(mySecondList))

myThirdList= []
#print(myThirdList)

myFourthList= []
t=0
while t<5:
    myFourthList.append(0)
    t=t+1
#print(myFourthList)

myFifthList= ["a", 5, "doodle", 3, 10]
#print(len(myFifthList))

mySixthList= ["a", 5, "doodle", 3, 10]
del mySixthList[2]
#print(mySixthList)

mySeventhList= ["a", 5, "doodle", 3, 10]
mySeventhList.append("money")
#print(mySeventhList)

myEighthList= ["a", 5, "doodle", 3, 10]
myEighthList[0]= "money"
#print(myEighthList)

myNinthList= ["a", 5, "doodle", 3, 10]
myNinthList[0]= "money " + "'a'"
print(myNinthList)