class Player:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def show_info(self):
        print(f"Player: {self.username} | Level: {self.level}")

    def level_up(self):
        self.level += 1
        print(f"{self.username} reached level {self.level}!")


player1 = Player("Agent_47", 10)
player2 = Player("Neo", 25)

print(player1.username)
print(player2.level)

player1.show_info()
player2.show_info()

player1.level_up()


class Weapon:
    damage = 50

    def __init__(self, name):
        self.name = name

    def fire(self):
        print(f"{self.name} is firing! Damage: {self.damage}")


pistol = Weapon("Glock")
pistol.fire()

print(isinstance(player1, Player))
print(hasattr(player2, "level"))

setattr(player1, "rank", "Elite")
print(getattr(player1, "rank"))

delattr(player1, "rank")


class EmptyClass:
    pass


empty_obj = EmptyClass()