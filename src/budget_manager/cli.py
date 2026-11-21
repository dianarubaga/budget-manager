"""Command-line interface for the personal budget manager."""
import argparse
from datetime import date
import sys
from pathlib import Path
from .services import add_transaction, report
from .storage import load_transactions, save_transactions

DEFAULT_DATA = Path("data/transactions.json")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Personal Budget Manager")
    parser.add_argument("--file", default=str(DEFAULT_DATA), help="JSON transaction file")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="Add a transaction")
    add.add_argument("kind", choices=["income", "expense"])
    add.add_argument("amount")
    add.add_argument("category")
    add.add_argument("--date", default=date.today().isoformat())
    commands.add_parser("list", help="List transactions")
    commands.add_parser("report", help="Show balance")
    args = parser.parse_args(argv)

    try:
        transactions = load_transactions(args.file)
        if args.command == "add":
            transactions, transaction = add_transaction(transactions, args.kind, args.category, args.amount, args.date)
            save_transactions(args.file, transactions)
            print(f"Added transaction {transaction.id}")
        elif args.command == "list":
            if not transactions:
                print("No transactions yet.")
            for item in transactions:
                print(f"{item.id} | {item.date} | {item.kind:7} | {item.category:13} | {item.amount:.2f} {item.currency}")
        elif args.command == "report":
            income, expenses, balance = report(transactions)
            print(f"Total income:   {income:.2f} EUR")
            print(f"Total expenses: {expenses:.2f} EUR")
            print(f"Balance:        {balance:.2f} EUR")
    except (ValueError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
