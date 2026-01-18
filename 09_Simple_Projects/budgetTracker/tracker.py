import json
import os

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, category, amount, trans_type):
        new_trans = {"category": category, "amount": amount, "type": trans_type}
        self.transactions.append(new_trans)

    def get_balance(self):
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == "Income")
        total_expense = sum(t['amount'] for t in self.transactions if t['type'] == "Expense")
        return total_income - total_expense

    def save_data(self, filename="data.json"):
        with open(filename, "w") as f:
            json.dump(self.transactions, f, indent=4)

    def load_data(self, filename="data.json"):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.transactions = json.load(f)