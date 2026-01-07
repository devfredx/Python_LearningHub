name = "Player1"
score = 95
print("Old Way: Hello %s, your score is %d." % (name, score))

health = 100
status = "Active"
print("Format Method: Player {} is currently {} with {} HP.".format(name, status, health))

print("Index Method: {0} has {1} HP. Go {0}!".format(name, health))

level = 5
experience = 1250.75
print(f"F-String: {name} reached Level {level} with {experience} XP.")

price = 49.99876
print(f"Formatted Price: ${price:.2f}") # Shows only 2 decimal places: $50.00

id_number = 7
print(f"User ID: {id_number:03d}") # Result: 007

# A simple Security/Game Log
user_ip = "192.168.1.105"
action = "LOGIN"
print("-" * 30)
print(f"LOG REPORT: [Action: {action:8}] | [Source: {user_ip}]")
print("-" * 30)