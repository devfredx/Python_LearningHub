class Transaction:
    def __init__(self, category, amount, type):
        self.category = category
        self.amount = amount
        self.type = type # "Income" or "Expense"