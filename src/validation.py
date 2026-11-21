"""Validate inputs before transactions enter the system."""
from datetime import date
from math import isfinite

CATEGORIES = {"food", "transport", "housing", "salary", "entertainment", "other"}
KINDS = {"expense", "income"}


def validate_transaction(kind, category, amount, date_text, currency="EUR"):
    if kind not in KINDS:
        raise ValueError("kind must be 'expense' or 'income'")
    if category not in CATEGORIES:
        raise ValueError(f"unknown category '{category}'; allowed: {', '.join(sorted(CATEGORIES))}")
    try:
        number = float(amount)
    except (TypeError, ValueError):
        raise ValueError("amount must be a number") from None
    if not isfinite(number) or number <= 0:
        raise ValueError("amount must be a finite number greater than 0")
    try:
        parsed = date.fromisoformat(date_text)
    except (TypeError, ValueError):
        raise ValueError("date must be a valid YYYY-MM-DD date") from None
    if parsed.isoformat() != date_text:
        raise ValueError("date must be formatted YYYY-MM-DD")
    if currency != "EUR":
        raise ValueError("this release supports EUR only")
    return number
