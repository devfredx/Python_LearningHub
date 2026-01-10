class Robot:
    def __init__(self, name, model, battery_level=100):
        self.name = name
        self.model = model
        self.battery_level = battery_level

    def status(self):
        print(f"Robot: {self.name} ({self.model}) - Battery: {self.battery_level}%")

r1 = Robot("R2D2", "Astromech")
r2 = Robot("C3PO", "Protocol", 45)

r1.status()
r2.status()

class Server:
    def __init__(self, ip):
        self.ip = ip
        self.services = []
        self.is_online = False
        print(f"Server {self.ip} initialized.")

    def start(self):
        self.is_online = True
        self.services.append("HTTP")
        print("Server is now online.")

web_server = Server("192.168.1.1")
web_server.start()

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p1 = Point()
p2 = Point(10, 20)

print(p1.x, p1.y)
print(p2.x, p2.y)

class Database:
    def __init__(self, db_name):
        self.name = db_name
        self.connection_string = f"connect://localhost/{db_name}"

db = Database("UsersDB")
print(db.connection_string)