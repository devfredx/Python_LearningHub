mixedList = ["python", 13, False, 90, 12.3 , "list"]

# to add an item to the end of the list
mixedList.append(3.14)
print(mixedList)

# to add item to a specific index
mixedList.insert(2, True)
print(mixedList)

# to add items from another list to the current list
list2 = [1,2,3,4,5,6]
mixedList.extend(list2)
print(mixedList)

# removes the specified item
mixedList.remove(False)
print(mixedList)

# removes the specified index
mixedList.pop(7)
print(mixedList)

del mixedList[0]
print(mixedList)

# removes last index
mixedList.pop()
print(mixedList)

# deletes the entire array and throws an error
# del mixedList
# print(mixedList)

# keeps the list but deletes the content
# mixedList.clear()
# print(mixedList)

# copies the list
x = mixedList.copy()
print(x)

# shows how many of the entered value are in the list
print(x.count(True))

# shows the index of the entered value in the list
print(x.index(3))

# reverses list order
x.reverse()
print(x)

# sorts the list alphabetically
languageList = ["python", "java", "c#", "ruby"]
languageList.sort()
print(languageList)