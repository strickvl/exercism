class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in row.split(" ")] for row in matrix_string.split("\n")]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        col = []
        for idx in range(1, len(self.matrix) + 1):
            row = self.matrix[idx - 1]
            col.append(row[index - 1])
        return col
