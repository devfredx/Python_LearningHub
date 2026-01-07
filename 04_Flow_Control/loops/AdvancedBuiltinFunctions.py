myList = [10,20,30,40,50,60,70]

print(list(range(30)))

for num in list(range(15)):
    print(num*2)

print(list(range(5,25)))
print(list(range(5,25,2)))

for indx in range(len(myList)):
    print(indx)

# enumerate
for element in enumerate(myList):
    print(element)

for (indx,value) in enumerate(myList):
    print(indx)

from random import randint
from random import shuffle

shuffle(myList)
print(myList)

print(randint(0,len(myList)))

# print(myList[range(0,len(myList)-1)])

# zip
foodList = ["apple", "banana", "melon"]
caloriesList = [100,150,200]
dayList = ["monday", "tuesday", "wednesday"]

zippedList = list(zip(foodList, caloriesList, dayList))

type(zippedList)
print(zippedList)

newList = []
myString = "metallica"

for elemant in myString:
    newList.append(elemant)
    print(newList)

# list comprehension
newList = [elemant for elemant in myString]
print(newList)

numbers = [10,20,30,40,50,60,70,80,90]
newNumberList = [num/2 for num in numbers]
print(newNumberList)

newNumberList = []
for num in numbers:
    newNumberList.append(num/2)
    print(newNumberList)