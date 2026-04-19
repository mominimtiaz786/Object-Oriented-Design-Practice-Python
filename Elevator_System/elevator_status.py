from enum import Enum


class DIRECTION(Enum):
    UP = "UP"
    DOWN = "DOWN"


class ElevatorStatus:
    def __init__(self, current_floor, direction: DIRECTION):
        self.current_floor = current_floor
        self.direction: DIRECTION = direction
    
    def getFloor(self):
        return self.current_floor
    
    def getDirection(self):
        return self.direction

    def updateDirection(self, target_floor: int):
        self.direction = DIRECTION.UP if target_floor > self.current_floor else DIRECTION.DOWN
            
