class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())

class File:
    def open(self):
        print("Opening a generic file")

class PDFFile(File):
    def open(self):
        print("Opening PDF with Adobe Reader")

class TextFile(File):
    def open(self):
        print("Opening TXT with Notepad")

files = [PDFFile(), TextFile()]

for f in files:
    f.open()

def start_engine(vehicle):
    vehicle.start()

class Car:
    def start(self):
        print("Car engine started with key")

class ElectricCar:
    def start(self):
        print("Electric car started with button")

my_car = Car()
my_tesla = ElectricCar()

start_engine(my_car)
start_engine(my_tesla)

print(len("Python"))
print(len([10, 20, 30, 40]))
print(len({"name": "Fred", "age": 25}))

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Square(4), Circle(3)]
for s in shapes:
    print(s.area())