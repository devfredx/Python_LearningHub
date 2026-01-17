import json
import os

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)

    def list_contacts(self):
        return self.contacts

    def search_contact(self, name):
        return [c for c in self.contacts if name.lower() in c['name'].lower()]

    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'].lower() != name.lower()]

    def save_to_file(self, filename="contacts.json"):
        with open(filename, "w") as f:
            json.dump(self.contacts, f, indent=4)

    def load_from_file(self, filename="contacts.json"):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.contacts = json.load(f)