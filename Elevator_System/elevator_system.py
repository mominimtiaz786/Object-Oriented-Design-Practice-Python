from . import (
    ElevatorStatus,
    ElevatorDispatch,
    ElevatorCar,
)
from .hallway_button_panel import HallwayButtonPanel
from .elevator_observer import ElevatorDispatchController

class ElevatorSystem:
    def __init__(self, dispatch_controller: ElevatorDispatch):
        self.elevators: list[ElevatorCar] = []
        self.dispatch_controller: ElevatorDispatch = dispatch_controller
        self.observer: ElevatorDispatchController = ElevatorDispatchController(dispatch_controller, self.elevators)
    

    def registerButtonPanel(self, panel: HallwayButtonPanel):
        panel.addObserver(self.observer)


    def getAllElevatorsStatuses(self)-> list[ElevatorStatus]:
        return map(lambda elevators: elevators.getStatus(), self.elevators)


    def requestElevator(self, current_floor: int, direction):
        self.dispatch_controller.dispatchElevatorCar(
            current_floor, direction, self.elevators
        )


    def selectFloor(self, current_elevator: ElevatorCar, floor_number: int):
        current_elevator.addFloorRequest(floor_number)


