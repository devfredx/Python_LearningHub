fitnessDictionary = {"banana":100,"apple":130}
print(type(fitnessDictionary))
print(len(fitnessDictionary))

dictionary = dict(name = "fred", age = 19, country = "TR")

print(fitnessDictionary["banana"])
print(fitnessDictionary.keys())
print(fitnessDictionary.values())

print(list(fitnessDictionary))

fitnessDictionary["banana"] = 180
print(fitnessDictionary)

fitnessDictionary["melon"] = 200
print(fitnessDictionary)

print(fitnessDictionary.get("appl",0))

myDictionary = {100:"a", 200:"b", 300:"c"}
print(myDictionary[200])

myDictionary = {"key1":"value1","key2":"value2","key3":"value3"}
print(myDictionary["key1"])

myMixedDictionary = {"key1":100,"key2":3.14,"key3":[10,20,30]}
print(myMixedDictionary["key3"])
print(myMixedDictionary["key3"][1])

dictionary2 = {"k1":10,"k2":[10,20,30,40,50],"k3":"string","k4":{"a":100,"b":200}}
print(dictionary2)

print(dictionary2["k2"][2])
print(dictionary2["k4"]["b"])