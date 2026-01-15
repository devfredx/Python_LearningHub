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

class Race:
    def __init__(self, race_name, track_length):
        self.race_name = race_name
        self.track_length = track_length
        self.participants = []

    def add_participant(self, vehicle):
        self.participants.append(vehicle)

    def check_winner(self):
        for v in self.participants:
            if v.distance_covered >= self.track_length:
                return v
        return None