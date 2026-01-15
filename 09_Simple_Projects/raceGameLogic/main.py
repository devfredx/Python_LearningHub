class Vehicle:
    def __init__(self, driver_name, team, top_speed):
        self.driver_name = driver_name
        self.team = team
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_covered = 0

    def get_info(self):
        return f"{self.driver_name} ({self.team}) - Top Speed: {self.top_speed} km/h"