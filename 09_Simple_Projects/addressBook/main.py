from address_book import AddressBook

def run():
    my_book = AddressBook()
    my_book.load_from_file()

    while True:
        print("\n--- ADDRESS BOOK ---")
        print("1. Add Contact\n2. List All\n3. Search\n4. Delete\n5. Exit")
        choice = input("Choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            my_book.add_contact(name, phone, email)
            my_book.save_to_file()
        elif choice == "2":
            contacts = my_book.list_contacts()
            for c in contacts:
                print(f"{c['name']} - {c['phone']}")
        elif choice == "3":
            results = my_book.search_contact(input("Search Name: "))
            print(results)
        elif choice == "4":
            my_book.delete_contact(input("Name to delete: "))
            my_book.save_to_file()
        elif choice == "5":
            break

if __name__ == "__main__":
    run()