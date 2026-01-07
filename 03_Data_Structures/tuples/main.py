# unchangeable
myTuple = (10, "a", 8.3, True, 9, "x")

print(len(myTuple))
print(type(myTuple))

tuple1 = ("python",)
print(type(tuple1))

# not a tuple
tuple2 = ("python")
print(type(tuple2))

tuple3 = tuple(("python", "java", "ruby"))
print(type(tuple3))

print(myTuple[1])
print(myTuple[-2])
print(myTuple[1:3])
print(myTuple[:4])
print(myTuple[2:])
print(myTuple[-3:-2])

if "a" in myTuple:
    print("Yes")
print()

# myTuple[1] = 200
# print(myTuple)

x = list(myTuple)
x[1] = "200"
myTuple = tuple(x)
print(x)
print()

x = list(myTuple)
x.append(False)
myTuple = tuple(x)
print(x)
print()

x = ("123",)
myTuple += x
print(myTuple)
print()

x = list(myTuple)
x.remove("123")
myTuple = tuple(x)
print(myTuple)
print()

# unpacking
(python, java, ruby) = tuple3
print(python)
print(java)
print(ruby)
print()

totalTuple = myTuple + tuple3
print(totalTuple)

tuple4 = totalTuple * 2
print(tuple4)
print()

# methods
numberTuple = (1,2,3,4,5,6,7,8,5)
x = numberTuple.count(5)
print(x)

x = numberTuple.index(8)
print(x)



