from enum import Enum


class LockerSize(Enum):
    SMALL = ("Small", float("5.00"), float("10.00"), float("10.00"), float("10.00"))
    MEDIUM = ("Medium", float("10.00"), float("20.00"), float("20.00"), float("20.00"))
    LARGE = ("Large", float("15.00"), float("30.00"), float("30.00"), float("30.00"))

    def __init__(self, size_name, daily_charge, width, height, depth):
        self.size_name = size_name
        self.daily_charge = daily_charge
        self.width = width
        self.height = height
        self.depth = depth

    def get_size_name(self):
        return self.size_name

    def get_daily_charge(self):
        return self.daily_charge

    def get_dimensions(self):
        return self.width, self.height, self.depth
