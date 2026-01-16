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

    def view_entries(self):
        for e in self.entries:
            print(f"[{e['date']}] | Mood: {e['mood']}\nContent: {e['content']}\n" + "-"*20)

    def search_entries(self, keyword):
        return [e for e in self.entries if keyword.lower() in e['content'].lower()]

    def show_stats(self):
        moods = [e['mood'] for e in self.entries]
        print("--- Mood Statistics ---")
        for m in set(moods):
            print(f"{m}: {moods.count(m)} times")