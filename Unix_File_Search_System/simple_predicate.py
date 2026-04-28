from __future__ import annotations
from typing import Generic, TypeVar
from .file_attribute import FileAttribute
from .file import File
from .comparison_operator import ComparisonOperator

T = TypeVar("T")


class SimplePredicate(Generic[T]):
    def __init__(self, attribute_name: FileAttribute, operator: ComparisonOperator[T], expected_value: T):
        self.attribute_name = attribute_name
        self.operator = operator
        self.expected_value = expected_value

    def isMatch(self, input_file: File) -> bool:
        actual_value = input_file.extract(self.attribute_name)

        if isinstance(actual_value, type(self.expected_value)):
            return self.operator.is_match(actual_value, self.expected_value)

        return False
