from vehicles.FedShip import FedShip
from vehicles.Klingon import Klingon


def status_report(ship):
    print('----------------------------------------------------')
    print('\t' + ship.__str__())
    print('----------------------------------------------------')


if __name__ == '__main__':
    fighter = FedShip()
    enemy = Klingon()

    status_report(fighter)
    status_report(enemy)

    fighter.shoot(enemy)
    enemy.shoot(fighter)

    status_report(fighter)
    status_report(enemy)
