from enum import Enum


class OrderStatus(Enum):
    QUEUED = "QUEUED"
    SENT_TO_KITCHEN = "SENT_TO_KITCHEN"
    SERVED = "SERVED"
    CANCELLED = "CANCELLED"
