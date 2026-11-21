
import unittest
import tempfile
from pathlib import Path


from budget_manager.models import Transaction
from budget_manager.validation import validate_transaction
from budget_manager.services import report
from budget_manager.storage import save_transactions, load_transactions



class TestBudgetManager(unittest.TestCase):

    # Test 1: Normal balance calculation
    def test_balance(self):
        transactions = [
            Transaction("T001", "2026-11-21", "income", "salary", 1500),
            Transaction("T002", "2026-11-21", "expense", "food", 20)
        ]

        income, expenses, balance = report(transactions)

        self.assertEqual(income, 1500)
        self.assertEqual(expenses, 20)
        self.assertEqual(balance, 1480)

    # Test 2: Reject negative amounts
    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            validate_transaction("expense", "food", -20, "2026-11-21")

    # Test 3: Reject invalid categories
    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            validate_transaction("expense", "shopping", 20, "2026-11-21")

    # Test 4: Reject invalid dates
    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            validate_transaction("expense", "food", 20, "2026-02-30")

    # Test 5: Save and load transactions
    def test_save_and_load(self):
        transactions = [
            Transaction("T001", "2026-11-21", "expense", "food", 20)
        ]

        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / "transactions.json"

            save_transactions(file, transactions)
            loaded = load_transactions(file)

            self.assertEqual(len(loaded), 1)
            self.assertEqual(loaded[0].amount, 20)
            self.assertEqual(loaded[0].category, "food")


if __name__ == "__main__":
    unittest.main()
