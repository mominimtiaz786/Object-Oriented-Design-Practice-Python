from __future__ import annotations
from .file_attribute import FileAttribute


class File:
    def __init__(self, size: int, filename: str, owner: str, is_directory: bool):
        self.size = size
        self.filename = filename
        self.owner = owner
        self.is_directory: bool = is_directory
        self.entries: set[File] = set()

    def extract(self, attribute_name: FileAttribute):
        if attribute_name in [
            FileAttribute.IS_DIRECTORY,
            FileAttribute.FILENAME,
            FileAttribute.SIZE,
            FileAttribute.OWNER,
        ]:
            return getattr(self, attribute_name.value)

        raise Exception("invalid filter criteria type")

    def addEntry(self, entry: File):
        self.entries.add(entry)

    def getEntries(self):
        return self.entries.copy()
