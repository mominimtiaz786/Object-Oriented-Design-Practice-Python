from __future__ import annotations

from TicTacToe_Game.board import Board
from TicTacToe_Game.game_status import GAME_STATUS
from TicTacToe_Game.player import Player
from TicTacToe_Game.score_tracker import ScoreTracker


class Game:
    def __init__(self, current_player_index=0):
        self.__board = Board()
        self.__score_tracker = ScoreTracker()
        self.__current_player_index = current_player_index
        self.__players: list[Player] = []

    def makeMove(self, colIndex: int, rowIndex: int, player: Player):
        if self.getGameStatus() in [GAME_STATUS.WIN, GAME_STATUS.DRAW]:
            raise Exception("game ended")

        if self.__players[self.__current_player_index] != player:
            raise Exception("not the current player")

        if self.__board.getPlayerAt(colIndex, rowIndex):
            raise Exception("board position is taken")

        self.__board.updateBoard(player, colIndex, rowIndex)

        self.__current_player_index = (self.__current_player_index + 1) % len(self.__players)
        if self.getGameStatus() in [GAME_STATUS.WIN, GAME_STATUS.DRAW]:
            self.__score_tracker.reportGameResult(self.__players[0], self.__players[1], self.__board.getWinner())

    def startNewGame(self, player1: Player, player2: Player) -> None:
        self.__board.reset()
        self.__players = [player1, player2]
        self.__current_player_index = 0

    def getScoreTracker(self) -> ScoreTracker:
        return self.__score_tracker

    def getGameStatus(self) -> GAME_STATUS:
        status = self.__board.checkStatus(self.__players[0])
        return status if status == GAME_STATUS.WIN else self.__board.checkStatus(self.__players[1])

    def getCurrentPlayer(self) -> Player:
        return self.__players[self.__current_player_index]
