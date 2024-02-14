mySet = {10,20,30,40,30,40,10,20}
print(mySet)

mySet = {10,20,30,40,30,40,10,20,True,1,2}
print(mySet)

mySet = {10,20,30,40,30,40,10,20,True,1,2,False,0}
print(mySet)

print(len(mySet))
print(type(mySet))

mySet2 = set(("a","b",1,2.3,False))
print(mySet2)

mySet2.add(True)
mySet2.add(15)
print(mySet2)

mySet.update(mySet2)
print(mySet)

myList = ["python", "java"]
mySet.update(myList)
print(mySet)

mySet.remove(False)
print(mySet)

mySet.discard(True)
print(mySet)

mySet.clear()
print(mySet)

del mySet
print(mySet)

set1 = {1,2,"3","4","50"}
set2 = {10,20,30,40,"50"}
set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

set1.intersection(set2)
print(set1)

set1.symmetric_difference_update(set2)
print(set1)