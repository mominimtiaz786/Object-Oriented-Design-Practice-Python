from .pricing_strategy import PricingStrategy

class Seat:
    def __init__(self, seat_number, pricing_strategy: PricingStrategy = None):
        self.number = seat_number
        self.pricing_strategy = pricing_strategy


    def get_pricing_strategy(self):
        return self.pricing_strategy


    def get_seat_number(self):
        return self.number