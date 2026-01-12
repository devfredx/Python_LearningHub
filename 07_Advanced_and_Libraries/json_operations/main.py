import json

data_string = '{"name": "Fred", "age": 25, "city": "Istanbul", "is_student": true}'
user_dict = json.loads(data_string)

print(user_dict["name"])
print(user_dict["city"])

profile = {
    "username": "devfredx",
    "level": 15,
    "inventory": ["sword", "shield", "potion"],
    "settings": {"music": False, "difficulty": "hard"}
}

json_output = json.dumps(profile, indent=4, sort_keys=True)
print(json_output)

with open("user_config.json", "w") as file:
    json.dump(profile, file, indent=4)

try:
    with open("user_config.json", "r") as file:
        loaded_data = json.load(file)
        print(loaded_data["username"])
except FileNotFoundError:
    print("File not found.")

numbers = [1, 2, 3, 4, 5]
print(json.dumps(numbers))

mixed_json = '[{"id": 1, "valid": true}, {"id": 2, "valid": false}]'
mixed_list = json.loads(mixed_json)
print(mixed_list[0]["id"])

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

u = User("Admin", "Superuser")
try:
    print(json.dumps(u))
except TypeError:
    print("Object of type User is not JSON serializable")

print(json.dumps(u.__dict__))