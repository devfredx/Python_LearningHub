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