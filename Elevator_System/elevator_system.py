from . import (
    ElevatorStatus,
    DispatchStrategy,
    ElevatorDispatch,
    ElevatorCar,
)

class ElevatorSystem:
    def __init__(self, dispatch_controller: DispatchStrategy):
        self.elevators: list[ElevatorCar] = []
        self.dispatch_controller: ElevatorDispatch = dispatch_controller
    

    def getAllElevatorsStatuses(self)-> list[ElevatorStatus]:
        return map(lambda elevators: elevators.getStatus(), self.elevators)


    def requestElevator(self, current_floor: int, direction):
        self.dispatch_controller.dispatchElevatorCar(
            current_floor, direction, self.elevators
        )


    def selectFloor(self, current_elevator: ElevatorCar, floor_number: int):
        current_elevator.addFloorRequest(floor_number)


