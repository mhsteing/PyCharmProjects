import random
import os
import time


class gameOfLife:

    def __init__(self, size):
        self.size = size
        self.matrix = [[random.randint(0,1) for row in range(0, size)] for column in range(0, size)]
        self.hilfs_matrix = [[0 for row in range(0, size)] for column in range(0, size)]

    def printToScreen(self):
        os.system("clear")
        for row in self.matrix:
            print(row)
        print("\n")

    def count_neighbours(self, row, column, size, matrix):
        neighbours = 0

        if row > 0:
            if column > 0:
                # north-west
                if matrix[row - 1][column - 1] == 1:
                     neighbours += 1

            # north
            if matrix[row-1][column] == 1:
                neighbours += 1

            if column < size - 1:
                # north-east
                if matrix[row-1][column+1] == 1:
                    neighbours += 1

        if row < size - 1:
            if column < size - 1:
                # south-east
                if matrix[row+1][column+1] == 1:
                    neighbours += 1

            # south
            if matrix[row+1][column] == 1:
                neighbours += 1

            if column > 0:
                # south-west
                if matrix[row+1][column-1] == 1:
                    neighbours += 1

        if column < size - 1:
            # east
            if matrix[row][column + 1] == 1:
                neighbours += 1

        if column > 0:
            # west
            if matrix[row][column-1] == 1:
                neighbours += 1

        return neighbours

    def rules(self, row, column, neighbours):
        matrix = self.matrix
        hilfmatrix = self.hilfs_matrix

        if matrix[row][column] == 0 and neighbours == 3:
            hilfmatrix[row][column] = 1

        elif matrix[row][column] == 1 and neighbours < 2:
            hilfmatrix[row][column] = 0

        elif matrix[row][column] == 1 and neighbours == 2 or neighbours == 3:
            hilfmatrix[row][column] = 1

        elif matrix[row][column] == 1 and neighbours > 3:
            hilfmatrix[row][column] = 0

        return hilfmatrix[row][column]

    def countCells(self, size):
        cells = 0
        for i in range(0, size):
            for j in range(0, size):
                if self.matrix[i][j] == 1:
                    cells += 1
        return cells

    def game(self, size):
        while True:
            print(f"Zellen: {self.countCells(size)}")
            self.printToScreen()
            for row in range(size):
                for column in range(size):
                    neighbours = self.count_neighbours(row, column, size, self.matrix)

                    self.hilfs_matrix[row][column] = self.rules(row, column, neighbours)
            self.matrix = self.hilfs_matrix
            time.sleep(1)






g = gameOfLife(10)
g.game(g.size)
