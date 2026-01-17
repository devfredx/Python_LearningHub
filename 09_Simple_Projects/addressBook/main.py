class AddressBook:
    def __init__(self):
        self.contacts = []

if __name__ == "__main__":
    my_book = AddressBook()
    print("Address Book Initialized.")

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }
        self.contacts.append(contact)
        print(f"Contact {name} added successfully!")

    def list_contacts(self):
        if not self.contacts:
            print("Address book is empty.")
        else:
            print("\n--- Contact List ---")
            for c in self.contacts:
                print(f"Name: {c['name']} | Phone: {c['phone']} | Email: {c['email']}")

if __name__ == "__main__":
    my_book = AddressBook()
    my_book.add_contact("John Doe", "555-0101", "john@email.com")
    my_book.list_contacts()

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)
        print(f"Contact {name} added.")

    def list_contacts(self):
        for c in self.contacts:
            print(f"Name: {c['name']} | Phone: {c['phone']}")

    def search_contact(self, name):
        results = [c for c in self.contacts if name.lower() in c['name'].lower()]
        return results

    def delete_contact(self, name):
        original_count = len(self.contacts)
        self.contacts = [c for c in self.contacts if c['name'].lower() != name.lower()]
        if len(self.contacts) < original_count:
            print(f"Contact {name} deleted.")
        else:
            print("Contact not found.")

if __name__ == "__main__":
    my_book = AddressBook()
    my_book.add_contact("Alice Smith", "555-0202", "alice@email.com")
    print(my_book.search_contact("Alice"))

import json
import os

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)

    def list_contacts(self):
        for c in self.contacts:
            print(f"Name: {c['name']} | Phone: {c['phone']}")

    def search_contact(self, name):
        return [c for c in self.contacts if name.lower() in c['name'].lower()]

    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'].lower() != name.lower()]

    def save_to_file(self, filename="contacts.json"):
        with open(filename, "w") as f:
            json.dump(self.contacts, f, indent=4)
        print("Data saved.")

    def load_from_file(self, filename="contacts.json"):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.contacts = json.load(f)
            print("Data loaded.")
import json
import os

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)

    def list_contacts(self):
        if not self.contacts:
            print("Empty book.")
        for c in self.contacts:
            print(f"Name: {c['name']} | Phone: {c['phone']} | Email: {c['email']}")

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

if __name__ == "__main__":
    my_book = AddressBook()
    my_book.load_from_file()

    while True:
        print("\n--- ADDRESS BOOK ---")
        print("1. Add Contact\n2. List All\n3. Search\n4. Delete\n5. Exit")
        choice = input("Choice: ")

        if choice == "1":
            my_book.add_contact(input("Name: "), input("Phone: "), input("Email: "))
            my_book.save_to_file()
        elif choice == "2":
            my_book.list_contacts()
        elif choice == "3":
            results = my_book.search_contact(input("Search Name: "))
            print(results)
        elif choice == "4":
            my_book.delete_contact(input("Name to delete: "))
            my_book.save_to_file()
        elif choice == "5":
            break