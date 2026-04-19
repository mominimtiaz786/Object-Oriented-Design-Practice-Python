from .elevator_observer import ElevatorObserver


class HallwayButtonPanel:

    def __init__(self, floor):
        self.floor = floor
        self.observers: list[ElevatorObserver] = []

    def pressButton(self, direction):
        self.notifyObservers(direction)

    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self, direction):
        for observer in self.observers:
            observer.update(self.floor, direction)
