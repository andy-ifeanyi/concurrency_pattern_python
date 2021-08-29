import random
import time

from oop.game_characters import Wizard, Creature


def print_header():
    print('----------------------------------')
    print('      WIZARD GAME APP             ')
    print('----------------------------------' + '\n')


def game_loop():
    creatures = [
        Creature('Toad', 1),
        Creature('Bat', 3),
        Creature('Tiger', 12),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000),
    ]

    hero = Wizard('Ozarki', 75)

    while creatures:
        active_creature = random.choice(creatures)
        print(f"A {active_creature.name} of level {active_creature.level} has just appeared!" + '\n')
        cmd = input('[a]ttack, [r]unaway, or [l]ookaround: ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The Wizard goes into rest and healing mode")
                time.sleep(2)
                print('The Wizard has returned!')
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print(f"{hero.name} looks around and sees: ")
            for c in creatures:
                print(f"* {c.name} of level {c.level}")
        else:
            print("Ok, exiting game... !")
            break


def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()
