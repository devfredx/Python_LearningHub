class Person():
    name = ""
    age = 0
    gender = ""

    #method, initializer
    def __init__(self):
        print("init executed")

myList = list()
print(type(myList))

fred = Person()
print(type(fred))

fred.name = "fred"
fred.age = 18
print(fred.name)
