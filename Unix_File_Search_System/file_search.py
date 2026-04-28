from __future__ import annotations
from .file import File
from .file_search_criteria import FileSearchCriteria


class FileSearch:
    def search(self, file: File, search_criteria: FileSearchCriteria):
        result: list[File] = []
        recursion_stack = [file]

        while recursion_stack:
            next_file = recursion_stack.pop()
            if search_criteria.isMatch(next_file):
                result.append(next_file)

            for entry in next_file.getEntries():
                recursion_stack.append(entry)

        return result
