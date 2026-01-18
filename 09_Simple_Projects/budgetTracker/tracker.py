class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, category, amount, trans_type):
        new_trans = {"category": category, "amount": amount, "type": trans_type}
        self.transactions.append(new_trans)