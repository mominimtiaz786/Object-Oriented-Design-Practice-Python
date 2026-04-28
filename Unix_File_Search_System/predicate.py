from __future__ import annotations
from abc import ABC, abstractmethod
from .file import File


class Predicate(ABC):
    @abstractmethod
    def isMatch(self, file: File) -> bool:
        pass
