import random


class Creature:
    def __init__(self, name, the_level):
        self.level = the_level
        self.name = name

    def __repr__(self):
        return f"{typename(self)}(name='{self.name}', the-level={self.level})"


class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name

    def __repr__(self):
        return f"{typename(self)}(name='{self.name}', the-level={self.level})"

    def attack(self, creature: Creature):
        print(f"The Wizard {self.name} attacks {creature.name}")

        # use a dice roll to determine winner
        wizard_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * self.level
        print(f"{self.name}'s dice roll: {wizard_roll}")
        print(f"{creature.name}'s dice roll: {creature_roll}")

        if wizard_roll >= creature_roll:
            print(f"The {self.name} has defeated the {creature.name}! ")
            return True
        else:
            print(f"The {self.name} has been defeated!")
            return False


def typename(obj):
    return type(obj).__name__
