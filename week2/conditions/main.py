x = 120
y = 99
if x > y:
    print("x greater than y")
elif x == y:
    print("x and y are equal")
else:
    print("y is greater than z")

print("x") if x > y else print("y")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

x = 41

if x > 10:
    print("Above ten")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

a = 33
b = 200

if b > a:
    pass

customerAge = 20
if customerAge < 18:
    print("you're not an adult yet")
elif customerAge > 18 and customerAge <= 30:
    print("you're middle-aged")
elif customerAge > 30:
    print("you're old")
else:
    print("your data is incorrect")

superheros = input("Enter a superhero: ")
if superheros  == "Superman":
    print("superman")
elif superheros == "Batman":
    print("Batman")
elif superheros == "Aquaman":
    print("Aquaman")
elif superheros == "Ironman":
    print("Ironman")
else:
    print(" :( ")

superheros2 = input("Enter a superhero: ")
superHero2List = ["Spiderman", "Ironman", "Thor", "Black Widow"]
if superheros2 in superHero2List:
    print("+")
else:
    print("-")
