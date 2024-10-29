class Car:
    def __init__(self, max_speed):
        self.maximum_speed = max_speed
        self.current_speed = 0
    def accelerate(self, change_of_speed):
        new_speed = self.current_speed + change_of_speed
        # Ensure new speed does not exceed the maximum_speed
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed
    def get_current_speed(self):
        return self.current_speed
car = Car(max_speed=100)
car.accelerate(30)
print("speed increased by +30 km/h:", car.get_current_speed())
car.accelerate(70)
print("speed increase by +70 km/h:", car.get_current_speed())
car.accelerate(50)
print("speed increase by +50 km/h:", car.get_current_speed())
car.accelerate(-200)
print("Current speed after emergency brake:", car.get_current_speed())
