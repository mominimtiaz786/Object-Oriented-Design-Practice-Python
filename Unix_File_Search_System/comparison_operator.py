from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar
import re

T = TypeVar("T")


class ComparisonOperator(ABC, Generic[T]):
    @abstractmethod
    def is_match(self, attribute_value: T, expected_value: T) -> bool:
        pass


class EqualsOperator(ComparisonOperator[T]):
    def is_match(self, attribute_value: T, expected_value: T) -> bool:
        return attribute_value == expected_value


class GreaterThanOperator(ComparisonOperator[float]):
    def is_match(self, attribute_value: float, expected_value: float) -> bool:
        return float(attribute_value) > float(expected_value)


class LessThanOperator(ComparisonOperator[float]):
    def is_match(self, attribute_value: float, expected_value: float) -> bool:
        return float(attribute_value) < float(expected_value)


class RegexMatchOperator(ComparisonOperator[str]):
    def is_match(self, attribute_value: str, expected_value: str) -> bool:
        return re.fullmatch(expected_value, attribute_value) is not None
