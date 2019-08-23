class SpaceShip(object):
    hp = 0
    atk = 0

    def shoot(self, enemy):
        enemy.hp = enemy.hp - self.atk