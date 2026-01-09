def check_status(status_code):
    match status_code:
        case 200:
            return "OK"
        case 400 | 404:
            return "Client Error"
        case 500:
            return "Server Error"
        case _:
            return "Unknown Status"

def process_command(command):
    match command.split():
        case ["quit"]:
            print("System shutting down...")
        case ["load", filename]:
            print(f"Loading file: {filename}")
        case ["move", x, y] if int(x) > 0 and int(y) > 0:
            print(f"Moving to positive coordinates: {x}, {y}")
        case ["move", x, y]:
            print(f"Moving to coordinates: {x}, {y}")
        case _:
            print("Command not recognized")

print(check_status(200))
print(check_status(404))

process_command("quit")
process_command("load data.json")
process_command("move 10 20")
process_command("move -5 0")

point = (0, 10)
match point:
    case (0, 0):
        print("Point is at the origin")
    case (0, y):
        print(f"Point is on the Y-axis at {y}")
    case (x, 0):
        print(f"Point is on the X-axis at {x}")
    case (x, y):
        print(f"Point is at {x}, {y}")

user_role = "admin"
match user_role:
    case "admin" | "root":
        print("Full access granted")
    case "user":
        print("Limited access granted")
    case _:
        print("Access denied")