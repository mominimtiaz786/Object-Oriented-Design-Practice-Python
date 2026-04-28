from __future__ import annotations
from abc import ABC
from .predicate import Predicate
from .file import File


class CompositePredicate(Predicate, ABC):
    pass


class AndPredicate(CompositePredicate):
    def __init__(self, operands: list[Predicate]):
        self.operands = operands

    def isMatch(self, file: File) -> bool:
        return len(self.operands) == sum(
            operand.isMatch(file) for operand in self.operands
        )


class OrPredicate(CompositePredicate):
    def __init__(self, operands: list[Predicate]):
        self.operands = operands

    def isMatch(self, file: File) -> bool:
        return 1 <= sum(
            operand.isMatch(file) for operand in self.operands
        )


class NotPredicate(CompositePredicate):
    def __init__(self, operand: Predicate):
        self.operand = operand

    def isMatch(self, file: File) -> bool:
        return not self.operand.isMatch(file)
