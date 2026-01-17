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