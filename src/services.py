"""Budget calculations independent of terminal and file operations."""
from .models import Transaction
from .validation import validate_transaction


def add_transaction(transactions, kind, category, amount, date_text):
    number = validate_transaction(kind, category, amount, date_text)
    next_number = max((int(t.id[1:]) for t in transactions), default=0) + 1
    transaction = Transaction(f"T{next_number:03d}", date_text, kind, category, number)
    return transactions + [transaction], transaction


def report(transactions):
    income = sum(t.amount for t in transactions if t.kind == "income")
    expenses = sum(t.amount for t in transactions if t.kind == "expense")
    return income, expenses, income - expenses
