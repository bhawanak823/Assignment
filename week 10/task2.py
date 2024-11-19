# Base Car class
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.kilometer_counter = 0

    def drive(self, hours):
        """Drives the car for the given number of hours at the current speed."""
        self.kilometer_counter += self.current_speed * hours

    def set_speed(self, speed):
        """Sets the current speed of the car."""
        if speed > self.max_speed:
            print(f"Speed {speed} exceeds max speed {self.max_speed}. Setting speed to max speed.")
            self.current_speed = self.max_speed
        else:
            self.current_speed = speed

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

def main():
    # Create one electric car and one gasoline car
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.set_speed(150)
    gasoline_car.set_speed(160)

    electric_car.drive(3)
    gasoline_car.drive(3)

    print(f"Electric car {electric_car.registration_number} has driven {electric_car.kilometer_counter} km.")
    print(f"Gasoline car {gasoline_car.registration_number} has driven {gasoline_car.kilometer_counter} km.")

if __name__ == "__main__":
    main()