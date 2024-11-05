class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def go_to_floor(self, target):
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Floor {self.current}")

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Floor {self.current}")

# Test
elevator = Elevator(0, 10)
elevator.go_to_floor(5)
elevator.go_to_floor(0)