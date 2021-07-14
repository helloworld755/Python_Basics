class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина едет')

    def stop(self):
        print('Машина стоит')

    def turn(self, direction):
        print('Машина повернула', direction)

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('Превышение скорости!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('Превышение скорости!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

a = TownCar(90, 'black', 'BMW', False)
b = SportCar(120, 'white', 'Ferrari', False)
c = WorkCar(60, 'red', 'Toyota', False)
d = PoliceCar(80, 'black', 'Audi', True)
a.go()
b.stop()
c.show_speed()
d.turn('налево')





