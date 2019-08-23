from random import randrange

from vehicles.SpaceShip import SpaceShip


class FedShip(SpaceShip):

    def __init__(self) -> None:
        self.hp = 100
        self.atk = randrange(20, 50)

    def __str__(self) -> str:
        return "A Federal spaceship with " \
               "attack power:{}, hp:{}".format(self.atk, self.hp)