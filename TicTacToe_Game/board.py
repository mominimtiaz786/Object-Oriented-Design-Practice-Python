from __future__ import annotations

from TicTacToe_Game.game_status import GAME_STATUS


class Board:
    def __init__(self, grid_size=3):
        self.__grid_size = grid_size
        self.__board = [([None]*grid_size)]*grid_size
        self.__turns = 0

    def printBoard(self):
        row_template = [" "]*(self.__grid_size*4+1)
        for i in range(0, self.__grid_size*4+1, 4):
            row_template[i]="|"

        boundary = "".join(([" ___"]*self.__grid_size))+" "

        for i in range(self.__grid_size):
            print(boundary)

            row = row_template.copy()

            index = 2
            for j in range(self.__grid_size):
               row[index] = self.__board[i][j] or " "
               index+=4

            print("".join(row))

        print(boundary)

    def updateBoard(self, player, row, col):
        if self.__board[row][col]:
            raise Exception(f"The Board place at ({row},{col} is already marked)")

        self.__board[row][col] = player
        self.__turns+=1

    def checkStatus(self, player):
        if self.__checkWin(player):
            return GAME_STATUS.WIN
        elif self.isFull():
            return GAME_STATUS.DRAW
        else:
            return GAME_STATUS.IN_PROGRESS

    def __checkWin(self, player):
        # check Rows
        for row in range(self.__grid_size):
            if self.__checkRowForWin(player, self.__board[row]):
                return True

        # Check Cols
        for col in range(self.__grid_size):
            if self.__checkRowForWin(player, [self.__board[i][col] for i in range(self.__grid_size)]):
                return True

        # Check Diagnoals
        diagnol_1 = [self.__board[i][i] for i in range(self.__grid_size)]
        diagnol_2 = [self.__board[i][self.__grid_size-1-i] for i in range(self.__grid_size)]

        if self.__checkRowForWin(player, diagnol_1) or self.__checkRowForWin(player, diagnol_2):
            return True

        return False

    def __checkRowForWin(self, player, row):
        for elm in row:
            if elm != player:
                return False

        return True

    def isFull(self):
        return self.__turns == self.__grid_size**2

    def getPlayerAt(self, row, col):
        return self.__board[row][col]

    def getWinner(self):
        for i in range(self.__grid_size):
            first = self.__board[i][0]
            if first and sum([first == c for c in self.__board[i]]) == self.__grid_size:
                return first

        for i in range(self.__grid_size):
            first = self.__board[0][i]
            if first and sum([
                    first == c for c in
                    [self.__board[j][i] for j in range(self.__grid_size)]
                ]) == self.__grid_size:
                return first

        first = self.__board[0][0]
        if first and sum([
                first == c for c in
                [self.__board[i][i] for i in range(self.__grid_size)]
            ]) == self.__grid_size:
            return first

        first = self.__board[0][self.__grid_size - 1]
        if first and sum([
                first == c for c in
                [self.__board[i][self.__grid_size-1-i] for i in range(self.__grid_size)]
            ]) == self.__grid_size:
            return first

        return None

    def reset(self):
        for i in range(self.__grid_size):
            for j in range(self.__grid_size):
                self.__board[i][j] = None
        self.__turns = 0
