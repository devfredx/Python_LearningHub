import json
import os

class PasswordManager:
    def __init__(self, file_path="passwords.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f)