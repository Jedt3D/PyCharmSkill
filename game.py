heroes = []


def save(hero):
    heroes.append(hero)


def strg_idx(mp, hp):
    return str(1.85 * mp / hp)


if __name__ == '__main__':
    satan = {'name': 'Mr.Satan', 'hp': 2500, 'mp': 1700}
    print(satan['name'] + '\n' + str(satan['hp']) + '\n' + str(satan['mp']) + '\n' + strg_idx(satan['mp'], satan['hp']))

    saiya = {'name': 'Vegita', 'hp': 9500, 'mp': 5900}
    print(saiya['name'] + '\n' + str(saiya['hp']) + '\n' + str(saiya['mp']) + '\n' + strg_idx(satan['mp'], satan['hp']))

    save(satan)
    save(saiya)
    print(heroes)
