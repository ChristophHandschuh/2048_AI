import numpy as np
import random


class gameClass():
    game_board = np.array((4, 4))

    def __init__(self):
        self.reset()

    def reset(self):
        self.game_board = np.zeros((4, 4), dtype=int)  # set board to 0
        self.addTiles()

    def addTiles(self):  # add two tiles on random position
        for _ in range(0, 2):
            while (True):
                x = random.randint(0, 3)
                y = random.randint(0, 3)
                if (self.game_board[x][y] == 0):
                    break
            self.game_board[x][y] = random.randint(1, 2) * 2

    def print_board(self):
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[i])):
                print(self.game_board[i][j], " ", sep="", end="")
            print()
        print()

    # Stack Function
    # Stack function iterates through each column of the board. It finds the first non - zero element in each column and stores its index in the 'k' variable.
    # Afterwards the method swaps the non - zero element with the current iteration position. Therefore, element are moved to the top.
    def stack(self, board):
        for i in range(0, 4):
            for j in range(0, 4):
                k = i
                while board[k][j] == 0:
                    if k == 3:
                        break
                    k += 1
                if k != i:
                    board[i][j], board[k][j] = board[k][j], 0

    # This function iterates through each cell column wise in the board. It checks if the current cell and the cell directly below have the same number.
    # If they do, the method adds two numbers together and sets the current cell and the cell below it to zero.
    # This process continues for the rest of the top row.
    def sum_up(self, board):
        for i in range(0, 3):
            for j in range(0, 4):
                if board[i][j] != 0 and board[i][j] == board[i + 1][j]:
                    board[i][j] += board[i + 1][j]
                    board[i + 1][j] = 0

    def move(self, direction):
        rotated_board = np.rot90(self.game_board, direction)
        self.stack(rotated_board)
        self.sum_up(rotated_board)
        self.stack(rotated_board)
        self.game_board = np.rot90(rotated_board, 4 - direction)
        self.addTiles()

    def score(self):
        return np.max(self.game_board)

    def gameOver(self):
        return np.count_nonzero(self.game_board == 0) < 2

    def flat(self):
        return self.game_board.flatten()
