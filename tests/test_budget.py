
import unittest
from src.models import Transaction
from src.validation import validate_transaction


class TestBudgetManager(unittest.TestCase):

    # Test 1: Normal transaction creation
    def test_create_transaction(self):
        transaction = Transaction(
            id="T001",
            date="2026-11-21",
            kind="expense",
            category="food",
            amount=20.0
        )

        self.assertEqual(transaction.amount, 20.0)
        self.assertEqual(transaction.category, "food")
        self.assertEqual(transaction.currency, "EUR")

    # Test 2: Convert transaction to a dictionary
    def test_transaction_to_dict(self):
        transaction = Transaction(
            id="T002",
            date="2026-11-21",
            kind="income",
            category="salary",
            amount=1500.0
        )

        result = transaction.to_dict()

        self.assertEqual(result["amount"], 1500.0)
        self.assertEqual(result["kind"], "income")

    # Test 3: Reject negative amounts
    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            validate_transaction(
                "2026-11-21", "expense", "food", -20
            )

    # Test 4: Reject invalid categories
    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            validate_transaction(
                "2026-11-21", "expense", "shopping", 20
            )


if __name__ == "__main__":
    unittest.main()
