class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_speed(self):
        print(f"The {self.brand} is going at {self.speed} km/h")

    def accelerate(self, increment):
        self.speed += increment
        self.display_speed()

car1 = Car("Tesla", 80)
car2 = Car("BMW", 100)

car1.accelerate(20)
car2.accelerate(10)

class User:
    def set_name(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

u = User()
u.set_name("Fred")
u.greet()

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count

c = Counter()
c.increment()
c.increment()
print(c.get_count())

class Comparison:
    def __init__(self, val):
        self.val = val

    def is_greater(self, other_obj):
        return self.val > other_obj.val

obj1 = Comparison(50)
obj2 = Comparison(30)
print(obj1.is_greater(obj2))