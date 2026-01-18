from tracker import BudgetTracker

def menu():
    tracker = BudgetTracker()
    tracker.load_data()

    while True:
        print(f"\nCurrent Balance: {tracker.get_balance()}")
        print("1. Add Income\n2. Add Expense\n3. Exit")
        choice = input("Select: ")

        if choice in ["1", "2"]:
            cat = input("Category: ")
            amt = float(input("Amount: "))
            t_type = "Income" if choice == "1" else "Expense"
            tracker.add_transaction(cat, amt, t_type)
            tracker.save_data()
        elif choice == "3":
            break

if __name__ == "__main__":
    menu()