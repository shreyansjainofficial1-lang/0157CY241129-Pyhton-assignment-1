class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def introduce(self):
        print(f"{self.name} has {self.health} health points.")

    def attack(self):
        print(f"{self.name} performs a basic attack.")

class Warrior(Character):
    def attack(self):
        print(f"{self.name} attacks with a sword.")

class Archer(Character):
    def attack(self):
        print(f"{self.name} shoots an arrow.")

class Mage(Character):
    def attack(self):
        print(f"{self.name} casts a magic spell.")

characters = [
    Warrior("Thor", 120),
    Archer("Robin", 90),
    Mage("Merlin", 80)
]

for character in characters:
    character.introduce()
    character.attack()
