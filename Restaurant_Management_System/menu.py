from __future__ import annotations

from .menu_item import MenuItem


class Menu:
    def __init__(self):
        self.items: dict[str, MenuItem] = {}

    def addItem(self, menu_item: MenuItem):
        self.items[menu_item.getName()] = menu_item

    def getItemByName(self, name: str) -> MenuItem | None:
        return self.items.get(name)

    def getMenuItems(self) -> list[MenuItem]:
        return list(self.items.values())
