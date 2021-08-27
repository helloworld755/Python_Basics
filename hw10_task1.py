class Matrix:
    def __init__(self, list_of_lists):
        self.n = len(list_of_lists)
        self.m = len(list_of_lists[0])
        self.matrix = list_of_lists

    def __str__(self):
        return '\n'.join('\t'.join(map(str, i)) for i in self.matrix)

    def __getitem__(self, i):
        return self.matrix[i]

    def __add__(self, other):
        result = []
        row = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = self.matrix[i][j] + other[i][j]
                row.append(summa)
                if len(row) == len(self.matrix[0]):
                    result.append(row)
                    row = []
        return Matrix(result)


a = [[0, 2], [5, 3], [6, 8]]
b = [[6, 1], [4, 9], [1, 2]]
mat_a = Matrix(a)
mat_b = Matrix(b)
mat_c = mat_a + mat_b
print(mat_c)
