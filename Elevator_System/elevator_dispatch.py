from . import (
    DIRECTION,
    DispatchStrategy,
    ElevatorCar,
)

class ElevatorDispatch:
    def __init__(self, strategy: DispatchStrategy):
        self.strategy: DispatchStrategy = strategy


    def dispatchElevatorCar(self, floor: int, direction: DIRECTION, all_elevators: list[ElevatorCar]):
        elevator = self.strategy.selectElevator(
            floor, direction, all_elevators
        )
        if elevator:
            elevator.addFloorRequest(floor)

