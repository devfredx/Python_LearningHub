class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self._salary = value
        else:
            print("Error: Invalid salary amount")

    @salary.deleter
    def salary(self):
        print("Deleting salary record...")
        del self._salary

emp = Employee("Fred", 5000)
print(emp.salary)

emp.salary = 6000
print(emp.salary)

emp.salary = -1000

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * (self.radius ** 2)

c = Circle(5)
print(c.radius)
print(c.area)

class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

u = User("John", "Doe")
print(u.full_name)

u.full_name = "Jane Smith"
print(u.first)
print(u.last)