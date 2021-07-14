class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self):
        return self._length * self._width * 25 * 5 / 1000

a = Road(20, 5000)
print(a.mass_calc(), ' т')
