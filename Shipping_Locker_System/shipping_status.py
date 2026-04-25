from enum import Enum


class ShippingStatus(Enum):
    CREATED = "CREATED"
    PENDING = "PENDING"
    IN_LOCKER = "IN_LOCKER"
    RETRIEVED = "RETRIEVED"
    EXPIRED = "EXPIRED"
