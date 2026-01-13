import json
import os
import secrets
import string

class PasswordManager:
    def __init__(self, file_path="passwords.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f)

    def generate_password(self, length=16):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def save_password(self, site, username, password):
        with open(self.file_path, "r") as f:
            data = json.load(f)
        data[site] = {"username": username, "password": password}
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def get_password(self, site):
        with open(self.file_path, "r") as f:
            data = json.load(f)
        return data.get(site, "Not found")

manager = PasswordManager()

while True:
    print("\n1. Generate & Save\n2. View Password\n3. Exit")
    choice = input("Select: ")

    if choice == "1":
        site = input("Website: ")
        user = input("Username: ")
        pwd = manager.generate_password()
        manager.save_password(site, user, pwd)
        print(f"Generated for {site}: {pwd}")
    elif choice == "2":
        site = input("Website: ")
        print(manager.get_password(site))
    elif choice == "3":
        break