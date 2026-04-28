import unittest

from Unix_File_Search_System.file import File
from Unix_File_Search_System.file_search import FileSearch
from Unix_File_Search_System.file_search_criteria import FileSearchCriteria
from Unix_File_Search_System.file_attribute import FileAttribute
from Unix_File_Search_System.simple_predicate import SimplePredicate
from Unix_File_Search_System.composite_predicate import AndPredicate
from Unix_File_Search_System.comparison_operator import EqualsOperator, RegexMatchOperator


class FileSearchTest(unittest.TestCase):
    def testFileSearch(self):
        # Create a root directory and two files with different owners
        root = File(size=0, filename="root", owner="adam", is_directory=True)
        a = File(size=2000, filename="a", owner="adam", is_directory=False)
        b = File(size=3000, filename="b", owner="george", is_directory=False)

        root.addEntry(a)
        root.addEntry(b)

        criteria = FileSearchCriteria(
            AndPredicate([
                SimplePredicate(
                    FileAttribute.IS_DIRECTORY,
                    EqualsOperator(),
                    False,
                ),
                SimplePredicate(
                    FileAttribute.OWNER,
                    RegexMatchOperator(),
                    r"ge.*",
                ),
            ])
        )

        file_search = FileSearch()
        result = file_search.search(root, criteria)

        self.assertEqual(1, len(result))
        self.assertEqual("b", result[0].filename)


if __name__ == "__main__":
    unittest.main()
