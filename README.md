# Interactive Personal Budget Manager — Release 1

A Python command-line application for recording income and expenses in EUR, listing transactions, and calculating total income, expenses, and remaining balance.

The application saves transactions in a JSON file so that data is preserved between sessions. It also supports undoing the last transaction.

## Project Structure

```text
budget-manager/
├── README.md
├── DESIGN.md
├── AI_DISCLOSURE.md
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
├── data/
│   ├── sample_transactions.csv
│   └── transactions.json
├── src/
│   └── budget_manager/
│       ├── __init__.py
│       ├── __main__.py
│       ├── models.py
│       ├── validation.py
│       ├── services.py
│       ├── storage.py
│       └── cli.py
└── tests/
    └── test_budget.py
```

## Setup with uv

This project uses `uv` to manage the Python environment and dependencies.

Clone the repository:

```bash
git clone https://github.com/dianarubaga/budget-manager.git
cd budget-manager
```

Set up the environment:

```bash
uv sync
```

No additional third-party Python libraries are required for the application.

## Run the Application

Display available commands:

```bash
uv run python -m budget_manager --help
```

### Add Transactions

Add €1,500 of income:

```bash
uv run python -m budget_manager add income 1500 salary --date 2026-11-21
```

Add €20 of food expenses:

```bash
uv run python -m budget_manager add expense 20 food --date 2026-11-21
```

Add €50 of transport expenses:

```bash
uv run python -m budget_manager add expense 50 transport --date 2026-11-21
```

If no date is provided, the current date is used.

### List Transactions

```bash
uv run python -m budget_manager list
```

Displays all recorded transactions, including their ID, date, type, category, amount, and currency.

### Generate a Report

```bash
uv run python -m budget_manager report
```

Expected output when starting with an empty dataset and adding the three example transactions:

```text
Total income:   1500.00 EUR
Total expenses: 70.00 EUR
Balance:        1430.00 EUR
```

### Undo the Last Transaction

The `undo` command removes the most recently added transaction:

```bash
uv run python -m budget_manager undo
```

For example, if the most recent transaction is a €50 transport expense, running `undo` removes it from the transaction list.

The updated data is immediately saved to the JSON file, so the removed transaction does not reappear when the application is restarted.

If no transactions exist, the program displays an error.

This feature implements the optional Undo Stretch Challenge from Practice 1.

## Data Storage

By default, transactions are saved in:

`data/transactions.json`

The application automatically loads existing transactions when started and saves updated data after adding or undoing a transaction.

The JSON file is created automatically when the first transaction is saved, if it does not already exist.

A different data file can be selected using `--file` before the command:

```bash
uv run python -m budget_manager --file data/example.json add expense 10 food
uv run python -m budget_manager --file data/example.json report
uv run python -m budget_manager --file data/example.json undo
```

## Input Validation

The application validates transactions before saving them.

- Transaction type must be `income` or `expense`.
- Amounts must be positive, finite numbers.
- Dates must be valid and formatted as `YYYY-MM-DD`.
- Allowed categories are `entertainment`, `food`, `housing`, `other`, `salary`, and `transport`.
- Only EUR is supported.
- Transaction IDs must be valid and unique when loading saved data.

Invalid inputs are rejected with an error message.

## Testing

The project uses Python's built-in `unittest` framework.

Run all automated tests:

```bash
uv run python -m unittest discover -s tests -v
```

The eight tests cover:

1. **Balance calculation:** Verifies income, expenses, and remaining balance.
2. **Negative amount:** Checks that negative amounts are rejected.
3. **Invalid category:** Checks that unknown categories are rejected.
4. **Invalid date:** Checks that impossible calendar dates are rejected.
5. **Save and load:** Verifies that transactions are correctly saved to and loaded from JSON.
6. **Undo transaction:** Checks that the last transaction is removed.
7. **Undo empty list:** Checks that undoing without transactions produces an error.
8. **Undo persistence:** Verifies that an undone transaction remains removed after saving and reloading the JSON file.

All eight tests passed during local testing.

### Manual Validation Example

Try adding a negative expense:

```bash
uv run python -m budget_manager add expense -5 food
```

The application should reject the transaction and display an error message.

## Sample Data

`data/sample_transactions.csv` contains representative transaction examples, including valid records and intentionally invalid cases for demonstrating input validation.

The application uses JSON for actual transaction storage. CSV import is not implemented in Release 1.

## Design

The application separates responsibilities across five modules:

- `models.py` — Defines the transaction data structure.
- `validation.py` — Checks user inputs and transaction data.
- `services.py` — Adds transactions, calculates balances, and implements undo.
- `storage.py` — Handles JSON saving and loading.
- `cli.py` — Processes terminal commands using `argparse`.

This structure keeps the command-line interface, business logic, and file operations separate, making the application easier to understand, maintain, and test.

A more detailed architectural explanation is provided in `DESIGN.md`.

## AI Disclosure

The use of AI assistance during development is documented in `AI_DISCLOSURE.md`.

## Known Limitations

- EUR only; no currency conversion.
- No CSV import or export.
- Undo only removes the last transaction; there is no redo or deletion of a selected transaction.
- No graphical interface.
- Monetary values use Python floating-point numbers rather than `Decimal`, which can introduce precision limitations.
- Designed for a single local user; simultaneous writes are not supported.

