class Elevator:
    def __init__ (self, bottom, top):
        self.current = bottom
        self.bottom, self.top = bottom, top

    def go_to_floor(self, target):
        while self.current < target: self.floor_up()
        while self.current > target: self.floor_down()

    def floor_up(self):
        if self.current < self.top: self.current += 1; print(f"Floor {self.current}")

    def floor_down(self):
        if self.current > self.bottom: self.current -= 1; print(f"Floor {self.current}")

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        print(f"\nElevator {elevator_number} moving to floor {target_floor}")
        self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        print("\nFire alarm! Moving all elevators to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"\nElevator {i} going to floor {elevator.bottom}")
            elevator.go_to_floor(elevator.bottom)

# Test
if __name__ == "__main__":
    # Create a building with floors from 0 to 10 and 3 elevators
    building = Building(0, 10, 3)

    # Run some elevators to various floors
    building.run_elevator(0, 5)
    building.run_elevator(1, 8)

    # Trigger the fire alarm
    building.fire_alarm()