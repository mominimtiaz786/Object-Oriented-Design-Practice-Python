from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from .enums import Action

if TYPE_CHECKING:
    from .hand import Hand


class PlayerDecisionLogic(ABC):
    @abstractmethod
    def decideAction(self, hand: Hand) -> Action:
        pass


class RealPlayerDecisionLogic(PlayerDecisionLogic):
    def decideAction(self, hand: Hand) -> Action:
        return Action.HIT if max(hand.getPossibleValues(), default=0) < 16 else Action.STAND


class DealerDecisionLogic(PlayerDecisionLogic):
    def decideAction(self, hand: Hand) -> Action:
        return Action.HIT if max(hand.getPossibleValues(), default=0) < 17 else Action.STAND
