class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if type(other) == Complex:
            n_1 = self.a + other.a
            n_2 = self.b + other.b
            return Complex(n_1, n_2)
        else:
            print('Error: Not the Complex type')

    def __mul__(self, other):
        if type(other) == Complex:
            n_1 = self.a * other.a - self.b * other.b
            n_2 = self.b * other.a + self.a * other.b
            return Complex(n_1, n_2)
        else:
            print('Error: Not the Complex type')

    def __str__(self):
        return f'({self.a}, {self.b})'

num_1 = Complex(1, 3)
num_2 = Complex(4, -5)
num_3 = num_1 + num_2
print(num_3)
num_1 = Complex(1, -1)
num_2 = Complex(3, 6)
num_3 = num_1 * num_2
print(num_3)
