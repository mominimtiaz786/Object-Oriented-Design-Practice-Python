from .layout import Layout

class Room:
    def __init__(self, room_number: str, layout: Layout):
        self.room_number = room_number
        self.layout: Layout = layout

    def get_layout(self):
        return self.layout
