from character.Saiya import Saiya
from character.Hero import Hero

if __name__ == '__main__':
    satan = Hero('Mr.Satan')
    satan.hp = 2500
    satan.mp = 1700
    satan.atk = 100
    saiya = Saiya('Vegita', 9500, 3900, 100)

    print(satan)
    print('Hero strength index = ' + satan.str_idx())
    print(saiya)
    print('Hero strength index = ' + saiya.str_idx())

    satan.attack(saiya)
    print(saiya)

    saiya.attack(satan)
    print(satan)

    saiya.super_saiya()
    print('Super Saiya Attack!!')
    saiya.attack(satan)
    print(satan)
