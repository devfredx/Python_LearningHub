message = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit."""
print(message)
print(len(message))

a = "Hello, World!"
print(a[12])

#for x in "fred":
#    print(x)
print()
print()

message = "python programming language"

print("python" in message)
if "python" in message:
    print("'python' is present.")

print("java" not in message)
if "java" not in message:
    print("'java' isn't present.")

print(message[4:22])
print(message[:5])
print(message[12:])
print(message[-12:-4])
print()
print()

print(message.upper())
#print(message.lower())
print(message.strip())
print(message.replace("p", "J"))

a = message.split(",")
print(a)

message2 = "string"
message3 = "operations"
totalMessage= message2 +" "+message3
print(totalMessage)

model = 'mtm'

brand = "this car is audi, model is " + model
print(brand)

message4 = 'this car is audi, model is {}'
print(message4.format(model))

hp = 1001
maxSpeed = "388 km/h"
price = '150k'
car = """This car is an audi. Model {}.
{} hp and a max speed of {}.
The market price is {} dollars."""
print()
print()
print(car.format(model,hp,maxSpeed,price))

print()
print()

car2 = "this car \"audi\" is expensive"
print(car2)

car2 = 'this car\'s expensive'
print(car2)

car2 = "this car \\ expensive"
print(car2)

car2 = 'this car\nis expensive'
print(car2)

car2 = 'this car\ris expensive'
print(car2)

car2 = 'this car\tis expensive'
print(car2)

car2 = 'this car \bis expensive'
print(car2)

car2 = 'this car\fis expensive'
print(car2)

