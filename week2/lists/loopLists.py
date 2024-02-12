mixedList = ["python", 13, False, 90, 12.3 , "list"]

# create a loop with a list
for x in mixedList:
    print(x)

print()

[print(x) for x in mixedList]

print()

# create a list-length loop
for i in range(len(mixedList)):
    print(mixedList[i])

print()

# write the values of the list to the output screen
# until the value of i reaches the number of elements of the list with while loop
i = 0
while i < len(mixedList):
    print(mixedList[i])
    i = i + 1

print()

# create a new list with list items containing the letter 'c'
languageList = ["python", "java", "c#", "ruby", "c++", "c", "javascript"]
newlist = []
for x in languageList:
    if "c" in x:
        newlist.append(x)
print(newlist)
# newlist = [x for x in languageList if "c" in x]

# create a new list with list items starting with the letter 'c'
newlist2 = []
for x in languageList:
    if x.startswith("c"):
        newlist2.append(x)
print(newlist2)
# newlist = [x for x in languageList if x.startswith("a")];

# only accepts products that are not "c"
newlist3 = [x for x in languageList if x != "c"]
print(newlist3)

# unconditional new list creation
newlist4 = [x for x in languageList]
print(newlist4)

# create a list containing as many vertices as the entered value
newlist5 = [x for x in range(8)]
print(newlist5)

# creates a list containing as many items as the value entered, subject to a condition
newlist6 = [x for x in range(23) if x < 14]
print(newlist6)

# set the values in the new list to upper case
newlist7 = [x.upper() for x in languageList]
print(newlist7)









