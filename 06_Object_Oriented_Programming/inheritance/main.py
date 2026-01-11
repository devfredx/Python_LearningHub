class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} is now ON.")

class Phone(Device):
    def __init__(self, brand, model, number):
        super().__init__(brand, model)
        self.number = number

    def call(self, contact):
        print(f"{self.brand} is calling {contact} from {self.number}")

class SmartPhone(Phone):
    def __init__(self, brand, model, number, os):
        super().__init__(brand, model, number)
        self.os = os

    def power_on(self):
        super().power_on()
        print(f"Loading {self.os}...")

my_phone = SmartPhone("Apple", "iPhone 15", "555-0101", "iOS")
my_phone.power_on()
my_phone.call("Alice")

class Scanner:
    def scan(self):
        print("Scanning document...")

class Printer:
    def print_doc(self):
        print("Printing document...")

class MultiFunctionPrinter(Scanner, Printer):
    def work(self):
        self.scan()
        self.print_doc()

mfp = MultiFunctionPrinter()
mfp.work()

print(issubclass(SmartPhone, Device))
print(issubclass(Phone, Device))
print(isinstance(my_phone, Device))