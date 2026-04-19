from abc import ABC, abstractmethod
import random
import math
from . import (
    DIRECTION,
    DispatchStrategy,
    ElevatorCar,
)

class DispatchStrategy(ABC):
    @abstractmethod
    def selectElevator(self, floor: int, direction: DIRECTION, all_elevators: list[ElevatorCar]) -> ElevatorCar:
        pass


class FirstComeFirstServeStrategy(DispatchStrategy):
    def selectElevator(self, floor: int, direction: DIRECTION, all_elevators: list[ElevatorCar]) -> ElevatorCar:
        for elevator in all_elevators:
            if elevator.isIdle() or elevator.getStatus().getDirection() == direction:
                return elevator

        # If no suitable elevator is found, randomly select one
        return all_elevators[random.randint(0, len(all_elevators)-1)]

class ShortestSeekTimeFirstStrategy(DispatchStrategy):
    def selectElevator(self, floor: int, direction: DIRECTION, all_elevators: list[ElevatorCar]) -> ElevatorCar:
        shortest_distance = float('inf')
        best_car = all_elevators[0]
        for elevator in all_elevators:
            distance = math.abs(elevator.getStatus().getFloor() - floor);
            if (elevator.isIdle() or elevator.getStatus().getDirection() == direction) and distance < shortest_distance:
                best_car =  elevator

        # If no suitable elevator is found, randomly select one
        return best_car