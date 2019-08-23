class Car():

    def __init__(self, model, brand, color, fuel) -> None:
        super().__init__()
        self.model = model
        self.brand = brand
        self.color = color
        self.fuel = fuel

    def __str__(self) -> str:
        return 'This is a {} {} from {} has {} litre left.'.format(self.color, self.model, self.brand, self.fuel)

    def drive(self, distance):
        self.fuel = self.fuel - (distance / 10)
    # 10 km ---> 1 litre
    # 200 km ---> x litre
    # x = 200/10


if __name__ == '__main__':
    camry = Car('Camry', 'Toyota', 'Red', 60)
    print(camry)

    print('Drive the car for 200km.')
    camry.drive(200)
    print(camry)

    # print('I saw a {} {}. Is that {}'.format(camry.color, camry.brand, camry.model))
