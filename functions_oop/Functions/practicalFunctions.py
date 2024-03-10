def divideNumber(number):
    return number / 2
print(divideNumber(20))

myList = [3,5,7,10,20,30]
myResultList = []

for num in myList:
    myResultList.append(divideNumber(num))
print(myResultList)

# map
print(list(map(divideNumber,myList)))

def controlString(string):
    return "python" in string

print(controlString("python language"))
print(controlString("java language"))

myStringList = ["python", "c#", "java", ".net", "python language"]
print(list(map(controlString, myStringList)))
print()

# filter
print(list(filter(controlString,myStringList)))

# lambda
multiplyLambda = lambda num : num * 3
print(type(multiplyLambda))

print(multiplyLambda(20))

result = multiplyLambda(10)
print(result)

numList = [10,20,30,40,50]
print(list(map(lambda num:num/4,numList)))

