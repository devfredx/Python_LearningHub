import json
from datetime import datetime

class Journal:
    def __init__(self):
        self.entries = []

        def add_entry(self, text, mood="Neutral"):
            entry = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "content": text,
                "mood": mood
            }
            self.entries.append(entry)
            print("Entry added successfully!")

            def save_to_file(self, filename="my_journal.json"):
                with open(filename, "w") as f:
                    json.dump(self.entries, f, indent=4)

            def load_from_file(self, filename="my_journal.json"):
                try:
                    with open(filename, "r") as f:
                        self.entries = json.load(f)
                except FileNotFoundError:
                    self.entries = []