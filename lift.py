class Lift:
    def __init__(self, highest_floor, max_riders=10):
        self.top_floor = highest_floor
        self.current_floor = 0
        self.capacity = max_riders
        self.num_riders = 0

    def get_top_floor(self):
        return self.top_floor

    def get_current_floor(self):
        return self.current_floor

    def get_capacity(self):
        return self.capacity

    def get_num_riders(self):
        return self.num_riders

    def is_full(self):
        return self.num_riders == self.capacity

    def add_riders(self, num_entering):
        if self.num_riders + num_entering <= self.capacity:
            self.num_riders += num_entering
        else:
            self.num_riders = self.capacity

    def go_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1

    def go_down(self):
        if self.current_floor > 0:
            self.current_floor -= 1

    def call(self, floor):
        if 0 <= floor <= self.top_floor:
            while self.current_floor != floor:
                if floor > self.current_floor:
                    self.go_up()
                else:
                    self.go_down()