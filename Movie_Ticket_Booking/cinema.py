from .room import Room

class Cinema:
    def __init__(self, addres: str, name: str):
        self.name = name
        self.address = addres
        self.rooms: list[Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

