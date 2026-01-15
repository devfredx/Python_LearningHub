import random
import time

class Vehicle:
    def __init__(self, driver_name, team, top_speed):
        self.driver_name = driver_name
        self.team = team
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_covered = 0

    def accelerate(self):
        boost = random.randint(20, 50)
        self.current_speed = min(self.top_speed, self.current_speed + boost)
        self.distance_covered += self.current_speed

class Race:
    def __init__(self, race_name, track_length):
        self.race_name = race_name
        self.track_length = track_length
        self.participants = []

    def add_participant(self, vehicle):
        self.participants.append(vehicle)

    def start(self):
        print(f"--- {self.race_name} Starting! ---")
        winner = None
        while not winner:
            for v in self.participants:
                v.accelerate()
                print(f"{v.driver_name} is at {v.distance_covered}m")
                winner = self.check_winner()
                if winner: break
            time.sleep(0.5)
        print(f"Winner: {winner.driver_name} from {winner.team}!")

    def check_winner(self):
        for v in self.participants:
            if v.distance_covered >= self.track_length:
                return v
        return None

v1 = Vehicle("Toprak Razgatlıoğlu", "BMW", 320)
v2 = Vehicle("Ayhancan Güven", "Porsche", 300)

gp = Race("Istanbul Park", 1000)
gp.add_participant(v1)
gp.add_participant(v2)
gp.start()