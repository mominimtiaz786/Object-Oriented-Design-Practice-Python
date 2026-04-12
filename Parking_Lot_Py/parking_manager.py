from Parking_Lot_Py.parking_spot import ParkingSpot
from Parking_Lot_Py.vehicle import Vehicle, VehicleSize


class ParkingManager:
    def __init__(self, available_spots: dict[VehicleSize, list[ParkingSpot]]):
        self.available_spots: dict[VehicleSize, list[ParkingSpot]] = available_spots
        self.vehicle_to_spot: dict[Vehicle, ParkingSpot] = {}
        self.spot_to_vehicle: dict[ParkingSpot, Vehicle] = {}


    def unpark_vehicle(self, vehicle: Vehicle):
        spot = self._get_parked_spot_by_vehicle(vehicle)
        if spot:
            self.spot_to_vehicle.pop(spot, None)
            spot.vacate_spot()
            self.available_spots[spot.get_size()].append(spot)


    def park_vehicle(self, vehicle: Vehicle)-> ParkingSpot:
            spot = self.find_spot_for_vehicle(vehicle)
            if spot:
                spot.occupy_spot(vehicle)
                self.vehicle_to_spot[vehicle] = spot
                self.spot_to_vehicle[spot] = vehicle
                return spot
            else:
                raise Exception("No available parking spot for this vehicle.")

    def _get_parked_spot_by_vehicle(self, vehicle: Vehicle) -> ParkingSpot:
        return self.vehicle_to_spot.get(vehicle, None)
    
    def _get_parked_vehicle_by_spot(self, spot: ParkingSpot) -> Vehicle:
        return self.spot_to_vehicle.get(spot, None)



    def find_spot_for_vehicle(self, vehicle: Vehicle) -> ParkingSpot:
        vehicle_size = vehicle.get_size()
        for size in VehicleSize:
            if size.value >= vehicle_size.value:
                if self.available_spots[size]:
                    return self.available_spots[size].pop(0)
        return None