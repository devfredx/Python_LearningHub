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
            print("Entry added successfully!")append(entry)