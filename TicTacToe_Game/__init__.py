from __future__ import annotations

"""
"Imagine you and a friend are sitting down for a quick game of Tic-Tac-Toe. You each choose a symbol (e.g., "X" or "O") and take turns placing your symbol on a board. After each move, the game checks if someone has won or if the board is full, signaling a draw. Behind the scenes, the game tracks your moves, updates a scoreboard to reflect wins, and maintains player rankings for future matches. Let's design a Tic-Tac-Toe game system that handles all this."

Requirements:
- The game is played on a 3x3 board.
- The system determines the game's status: a win, a draw, or in progress.
- A score tracker records player performance, updates ratings based on wins, and supports queries like rankings or top players.
- Invalid moves (e.g., placing a symbol in an occupied cell) are rejected with feedback to the player.
"""

from TicTacToe_Game.game_status import GAME_STATUS
from TicTacToe_Game.player import Player
from TicTacToe_Game.board import Board
from TicTacToe_Game.score_tracker import ScoreTracker
from TicTacToe_Game.game import Game

__all__ = ["GAME_STATUS", "Player", "Board", "ScoreTracker", "Game"]
