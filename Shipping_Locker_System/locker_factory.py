from .locker import Locker
from .locker_size import LockerSize


class LockerFactory:
    @staticmethod
    def createLocker(size: str) -> Locker:
        match size:
            case "SMALL":
                return Locker(LockerSize.SMALL)
            case "MEDIUM":
                return Locker(LockerSize.MEDIUM)
            case "LARGE":
                return Locker(LockerSize.LARGE)
