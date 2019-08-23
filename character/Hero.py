class Hero():

    def __init__(self, name: str, hp: int, mp: int, atk: int):
        """
        Super Hero Class
        :param name: Hero name
        :param hp: Health Power
        :param mp: Magic Power
        :param atk: Attack Score
        """
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk

    def __str__(self) -> str:
        return """This hero is {} who has...
        HP:{}
        MP:{}""".format(self.name.upper(), self.hp, self.mp)

    def str_idx(self):
        return '{:.2f}'.format(1.85 * self.mp / self.hp)

    def attack(self, enemy):
        enemy.hp = enemy.hp - self.atk
