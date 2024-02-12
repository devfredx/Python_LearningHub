list1 = ["python", "java", "c#"]
list2 = [4, 6, 2, 11, 8]
list3 = [False, True, False]
mixedList = ["python", 13, False, 90, 12.3 , "list"]
numberList = list((1,2,3,4,5,6,7,8,9))


print(mixedList[0])
print(numberList)

print(len(mixedList))
print(type(mixedList))

print(list1[0])
print(list1[-1])

print(numberList[3:7])
print(numberList[:4])
print(numberList[6:])
print(numberList[-4:-1])
print()

if 5 in numberList:
    print("5 available in the list")
print()

mixedList[1] = True
print(mixedList)

mixedList[1:4] = [0.99, "true", False, 2]
print(mixedList)

mixedList[1:4] = [0.99, "true", False, 2, 12, 27, 36, 45]
print(mixedList)

mixedList[1:4] = [200]
print(mixedList)