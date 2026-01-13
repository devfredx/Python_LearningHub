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