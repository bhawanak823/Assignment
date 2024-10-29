class Car:
    def __init__(self, registration_num, max_speed):
        self.registration_number = registration_num
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car(registration_num="ABC-123", max_speed=142)
print(f"Registration Number: {car.registration_number}")
print(f"Max Speed: {car.maximum_speed} km/h")
print(f"Current Speed: {car.current_speed} km/h")
print(f"Travelled Distance: {car.travelled_distance} km")
