from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .table import Table


class Reservation:
    def __init__(self, party_name: str, party_size: int, table: "Table", reserved_time: datetime):
        self.party_name = party_name
        self.party_size = party_size
        self.table = table
        self.reserved_time = reserved_time

    def getTime(self) -> datetime:
        return self.reserved_time

    def getPartyName(self) -> str:
        return self.party_name

    def getTable(self) -> "Table":
        return self.table

    def getPartySize(self) -> int:
        return self.party_size
