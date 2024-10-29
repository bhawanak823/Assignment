class Car:
    def __init__(self, max_speed):
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def drive(self, hours):
        # Increase travelled_distance based on current_speed and hours
        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled
    def get_current_speed(self):
        return self.current_speed
    def get_travelled_distance(self):
        return self.travelled_distance
# let the car's maximum speed is 140 km/h
car = Car(max_speed=140)
# Set initial conditions as per example
car.travelled_distance = 2000
car.current_speed = 60
car.drive(1.5)
print("Travelled distance after driving for 1.5 hours:", car.get_travelled_distance())
