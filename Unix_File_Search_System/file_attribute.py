from enum import Enum


class FileAttribute(Enum):
    IS_DIRECTORY = "is_directory"
    FILENAME = "filename"
    SIZE = "size"
    OWNER = "owner"
