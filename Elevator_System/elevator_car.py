from . import (
    ElevatorStatus,
    DIRECTION,
)

class ElevatorCar:
    def __init__(self, starting_floor=0):
        self.status: ElevatorStatus = ElevatorStatus(starting_floor, DIRECTION.UP)
        self.target_floors: list[int] = []
        

    def getStatus(self)-> ElevatorStatus:
        return self.status


    def addFloorRequest(self, floor: int):
        if floor not in self.target_floors:
            self.target_floors.append(floor)
            self.updateDirection(floor)


    def isIdle(self):
        return not len(self.target_floors)


    def updateDirection(self, target_floor: int):
        if self.status.getCurrentFloor() < target_floor:
            status = ElevatorStatus(status.getCurrentFloor(), DIRECTION.UP)

        elif self.status.getCurrentFloor() > target_floor:
            status = ElevatorStatus(status.getCurrentFloor(), DIRECTION.DOWN);

