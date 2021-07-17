class Cell:
    def __init__(self, cell_cell):
        self.cell_cell = cell_cell

    def __add__(self, other):
        if type(other) == Cell:
            return Cell(self.cell_cell + other.cell_cell)
        else:
            print('Error: Not the Cell type')

    def __sub__(self, other):
        if type(other) == Cell:
            if self.cell_cell - other.cell_cell > 0:
                return Cell(self.cell_cell - other.cell_cell)
            else:
                return print('Error: Difference is less than zero')
        else:
            print('Error: Not the Cell type')

    def __mul__(self, other):
        if type(other) == Cell:
            return Cell(self.cell_cell * other.cell_cell)
        else:
            print('Error: Not the Cell type')

    def __floordiv__(self, other):
        if type(other) == Cell:
            return Cell(self.cell_cell // other.cell_cell)
        else:
            print('Error: Not the Cell type')

    def __str__(self):
        return f'{self.cell_cell}'

    def make_order(self, num):
        str = ''
        for i in range(self.cell_cell):
            str += '*'
            if (i + 1) % num == 0:
                str += '\n'
        print(str)


a = Cell(15)
b = Cell(10)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
a.make_order(4)