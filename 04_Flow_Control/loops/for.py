numbers = [10,11,12,13,14,15,16,17,18]
for num in numbers:
    print(num * 2)
print("\n")

for num in numbers:
    if num % 6 == 0:
        print(num)

myString = "python"
for s in myString:
    print(s)

myTuple = (10,20,30,40,50,60,70)
for t in myTuple:
    print(t / 5 * 2)

myList = [("a","b"),("c","d"),("e","f"),("g","h")]
for elemant in myList:
    print(elemant)

for (x,y) in myList:
    print(x)

mySet = {1,2,3,4,5}
for num in mySet:
    print(num)

myDictionary = {"k1":100,"k2":200,"k3":300,}
for (key,value) in myDictionary.items():
    print(value)

print("\n")

for number in numbers:
    print(number)
    if number==15:
        print("yes")
        break;

print("\n")

for number in numbers:
    print(number)
    if number==14:
        print("yes")
        continue;

for number in myList:
    pass

for x in range(6):
    print(x)
for x in range(2, 6):
    print(x)
for x in range(2, 30, 3):
    print(x)
