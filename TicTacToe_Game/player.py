from __future__ import annotations


class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    def getSymbol(self):
        return self.symbol

    def getName(self):
        self.name
