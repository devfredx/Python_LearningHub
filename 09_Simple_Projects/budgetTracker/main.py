from tracker import BudgetTracker

def menu():
    tracker = BudgetTracker()
    tracker.load_data()

    while True:
        try:
            print(f"\n--- Budget Tracker ---")
            print(f"Current Balance: {tracker.get_balance()}")
            print("1. Add Income\n2. Add Expense\n3. List All\n4. Exit")
            choice = input("Select: ")

            if choice in ["1", "2"]:
                cat = input("Category: ")
                amt = float(input("Amount: "))
                t_type = "Income" if choice == "1" else "Expense"
                tracker.add_transaction(cat, amt, t_type)
                tracker.save_data()
            elif choice == "3":
                for t in tracker.transactions:
                    print(f"{t['type']}: {t['category']} - {t['amount']}")
            elif choice == "4":
                break
        except ValueError:
            print("Please enter a valid number for amount!")

if __name__ == "__main__":
    menu()