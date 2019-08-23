from calculator.circle import circle_area
from calculator.sphere import sphere_volume


def calc(calc_type, radius):
    if calc_type == 'circle':
        return circle_area(radius)
    elif calc_type == 'sphere':
        return sphere_volume(radius)
    else:
        return 'Invalid'


if __name__ == '__main__':
    print(calc('circle', 25))
    print(calc('sphere', 25))
    print(calc('adsfasdf', 25))
