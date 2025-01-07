import datetime
class ParkingLot:
    def __init__(self, num_spaces):
       
        self.num_spaces = num_spaces
        self.available_spaces = num_spaces
        self.occupied_spaces = 0
        self.vehicles = {}  # Dictionary to store vehicle information

    def check_in(self, vehicle_id):
       
        if self.available_spaces > 0:
            self.vehicles[vehicle_id] = {'check_in_time': datetime.datetime.now()}
            self.available_spaces -= 1
            self.occupied_spaces += 1
            print(f"Vehicle {vehicle_id} checked in successfully.")
            return True
        else:
            print("Parking lot is full. Check-in failed.")
            return False

    def check_out(self, vehicle_id):
        
        if vehicle_id in self.vehicles:
            check_in_time = self.vehicles[vehicle_id]['check_in_time']
            check_out_time = datetime.datetime.now()
            parking_duration = check_out_time - check_in_time
            print(f"Vehicle {vehicle_id} checked out.")
            print(f"Parking duration: {parking_duration}")
            del self.vehicles[vehicle_id]
            self.available_spaces += 1
            self.occupied_spaces -= 1
            return True
        else:
            print(f"Vehicle {vehicle_id} not found in the parking lot.")
            return False

    def display_status(self):
       
        print(f"Available spaces: {self.available_spaces}")
        print(f"Occupied spaces: {self.occupied_spaces}")

if __name__ == "__main__":
    parking_lot = ParkingLot(10)

    parking_lot.check_in("Car1")
    parking_lot.check_in("Car2")
    parking_lot.check_out("Car1")
    parking_lot.check_in("Car3")

    parking_lot.display_status()