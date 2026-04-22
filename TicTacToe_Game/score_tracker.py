from __future__ import annotations

from TicTacToe_Game.player import Player


class ScoreTracker:
    def __init__(self):
        self.player_ratings: dict[Player, int] = {}

    def getTopPlayers(self) -> dict[Player, int]:
        return dict(sorted(
                self.player_ratings.items(),
                reverse=True,
                key=lambda x: x[1]
                )
            )

    def reportGameResult(self, player1: Player, player2: Player, winner=None):
        if winner:
            winner, loser = player1, player2 if winner == player1 else player2, player1
            self.player_ratings[winner] = self.player_ratings.get(winner, 0) + 1
            self.player_ratings[loser] = self.player_ratings.get(loser, 0) + 1

    def getRank(self, player: Player):
        if player not in self.player_ratings:
            return 0
        return list(
            sorted(
                self.player_ratings.keys(),
                reverse=True,
                key=lambda x: self.player_ratings[x]
                )
            ).index(player)
