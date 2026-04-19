from abc import ABC, abstractmethod
from .elevator_dispatch import ElevatorDispatch
from .elevator_car import ElevatorCar
from .elevator_status import DIRECTION


class ElevatorObserver(ABC):
    @abstractmethod
    def update(self, floor: int, direction: DIRECTION):
        pass


class ElevatorDispatchController(ElevatorObserver):
    def __init__(self, dispatch: ElevatorDispatch, elevators: list[ElevatorCar]):
        self.dispatch = dispatch
        self.elevators = elevators

    def update(self, floor: int, direction: DIRECTION):
        self.dispatch.dispatchElevatorCar(floor, direction, self.elevators)
