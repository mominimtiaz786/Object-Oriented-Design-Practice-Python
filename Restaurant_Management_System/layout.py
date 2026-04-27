from __future__ import annotations

from collections import defaultdict
from datetime import datetime

from .table import Table


class Layout:
    def __init__(self, table_capacities: list[int] = []):
        self.tables_by_id: dict[str, Table] = {}
        self.tables_by_cap: dict[int, set[Table]] = defaultdict(set)
        for capacity in table_capacities:
            self.addTable(capacity)

    def findAvailableTable(self, party_size: int, party_time: datetime) -> Table | None:
        sorted_caps = sorted(cap for cap in self.tables_by_cap if cap >= party_size)
        for cap in sorted_caps:
            for table in self.tables_by_cap[cap]:
                if table.isAvailableAt(party_time):
                    return table
        return None

    def addTable(self, table_capacity: int):
        table_id = f"TABLE-{len(self.tables_by_id) + 1}"
        table = Table(table_id, table_capacity)
        self.tables_by_id[table_id] = table
        self.tables_by_cap[table_capacity].add(table)
