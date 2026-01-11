class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            print("Insufficient funds or invalid amount")
            return 0

    def get_balance(self):
        return self.__balance

account = BankAccount("John Doe", 1000)

print(account.owner)
account.deposit(500)
print(account.get_balance())

# print(account.__balance)  # This would raise an AttributeError

class SoftwareProject:
    def __init__(self):
        self._version = "1.0.0"
        self.__security_key = "SECRET123"

    def get_key(self):
        return self.__security_key

    def set_key(self, new_key):
        if len(new_key) > 5:
            self.__security_key = new_key

project = SoftwareProject()
print(project._version)
print(project.get_key())

class Parent:
    def __init__(self):
        self._protected_var = 10
        self.__private_var = 20

class Child(Parent):
    def display(self):
        print(self._protected_var)
        # print(self.__private_var)  # This would raise an AttributeError

c = Child()
c.display()

print(account._BankAccount__balance)s