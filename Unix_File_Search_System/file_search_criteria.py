from __future__ import annotations
from .file import File
from .predicate import Predicate


class FileSearchCriteria:
    def __init__(self, predicate: Predicate):
        self.predicate: Predicate = predicate

    def isMatch(self, file: File):
        return self.predicate.isMatch(file)
