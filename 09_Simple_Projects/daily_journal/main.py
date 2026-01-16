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
            print(f"[{e['date']}] | Mood: {e['mood']}\nContent: {e['content']}\n" + "-" * 20)

    def search_entries(self, keyword):
        return [e for e in self.entries if keyword.lower() in e['content'].lower()]

    def show_stats(self):
        moods = [e['mood'] for e in self.entries]
        print("--- Mood Statistics ---")
        for m in set(moods):
            print(f"{m}: {moods.count(m)} times")

    def check_pin(self, pin):
        return pin == "1234"


if __name__ == "__main__":
    my_journal = Journal()
    my_journal.load_from_file()

    if my_journal.check_pin(input("Enter PIN: ")):
        while True:
            print("\n1. Add Entry\n2. View All\n3. Search\n4. Stats\n5. Exit")
            choice = input("Select: ")
            if choice == "1":
                txt = input("Content: ")
                md = input("Mood: ")
                my_journal.add_entry(txt, md)
                my_journal.save_to_file()
            elif choice == "2":
                my_journal.view_entries()
            elif choice == "3":
                results = my_journal.search_entries(input("Search for: "))
                print(results)
            elif choice == "4":
                my_journal.show_stats()
            elif choice == "5":
                break
    else:
        print("Wrong PIN!")