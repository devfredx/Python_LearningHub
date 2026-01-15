import random

class Vehicle:
    def __init__(self, driver_name, team, top_speed):
        self.driver_name = driver_name
        self.team = team
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_covered = 0

    def accelerate(self):
        boost = random.randint(10, 30)
        self.current_speed = min(self.top_speed, self.current_speed + boost)
        self.distance_covered += self.current_speed

    def get_info(self):
        return f"{self.driver_name} ({self.team}) - Distance: {self.distance_covered} km"