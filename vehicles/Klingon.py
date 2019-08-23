from random import randrange

from vehicles.SpaceShip import SpaceShip


class Klingon(SpaceShip):

    def __init__(self) -> None:
        self.hp = 120
        self.atk = randrange(20, 40)

    def __str__(self) -> str:
        return "A Klingon spaceship with " \
               "attack power:{}, hp:{}".format(self.atk, self.hp)