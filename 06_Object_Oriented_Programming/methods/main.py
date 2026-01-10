class GameCharacter:
    base_power = 10

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage. Health: {self.health}")

    @classmethod
    def update_base_power(cls, new_power):
        cls.base_power = new_power
        print(f"Global base power updated to: {cls.base_power}")

    @staticmethod
    def is_valid_name(name):
        return len(name) >= 3 and name.isalnum()


char1 = GameCharacter("Warrior", 100)
char1.take_damage(20)

GameCharacter.update_base_power(15)
print(char1.base_power)

print(GameCharacter.is_valid_name("Hero123"))
print(GameCharacter.is_valid_name("H!"))


class MathOps:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(MathOps.add(5, 10))


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        day, month, year = map(int, date_str.split("-"))
        return cls(day, month, year)


my_date = Date.from_string("10-01-2026")
print(my_date.year) 