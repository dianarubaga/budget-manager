# Interactive Personal Budget Manager — Release 1

A Python command-line application that allows users to record income and expenses, view their transactions, and calculate their total income, expenses, and remaining balance.

The application uses EUR as its currency and saves transactions in a JSON file so that data is preserved between sessions.

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

Display the available commands:

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

Add €50 of transportation expenses:

```bash
uv run python -m budget_manager add expense 50 transport --date 2026-11-21
```

If no date is provided, the program uses the current date.

### List Transactions

```bash
uv run python -m budget_manager list
```

This displays all recorded transactions, including their ID, date, type, category, amount, and currency.

### Generate a Report

```bash
uv run python -m budget_manager report
```

For an initially empty dataset containing only the three example transactions, the expected output is:

```text
Total income:   1500.00 EUR
Total expenses: 70.00 EUR
Balance:        1430.00 EUR
```

## Data Storage

Transactions are automatically saved in:

`data/transactions.json`

The program loads existing transactions when it starts and saves updated data after adding a transaction.

The JSON file is created automatically when the first transaction is successfully saved, if it does not already exist.

A different data file can be specified using `--file` before the command:

```bash
uv run python -m budget_manager --file data/example.json add expense 10 food
uv run python -m budget_manager --file data/example.json report
```

## Input Validation

The application checks user input before creating a transaction.

- Transaction type must be `income` or `expense`.
- Amounts must be positive.
- Dates must be valid and follow the `YYYY-MM-DD` format.
- Categories must be one of: `entertainment`, `food`, `housing`, `other`, `salary`, or `transport`.

Invalid inputs produce an error message instead of being saved.

## Testing

Automated tests are implemented using Python's built-in `unittest` module.

Run them with:

```bash
uv run python -m unittest discover -s tests -v
```

The five tests cover:

1. **Normal balance calculation:** Verifies income, expenses, and remaining balance.
2. **Negative amount:** Checks that negative amounts are rejected.
3. **Invalid category:** Checks that unknown categories are rejected.
4. **Invalid date:** Checks that impossible calendar dates are rejected.
5. **Save and load:** Verifies that transactions can be saved to JSON and loaded correctly.

All five tests passed during local testing.

### Manual Validation Example

Try entering a negative expense:

```bash
uv run python -m budget_manager add expense -5 food
```

The application should display an error and reject the transaction.

## Sample Data

`data/sample_transactions.csv` provides the transaction column structure for example data and validation cases.

The application currently uses JSON for saving and loading transactions. Importing CSV files is not implemented in Release 1.

## Design

The application separates responsibilities into five modules:

- `models.py` — Defines the transaction data structure.
- `validation.py` — Checks transaction inputs and provides error messages.
- `services.py` — Adds transactions and calculates income, expenses, and balance.
- `storage.py` — Handles saving and loading JSON files.
- `cli.py` — Processes terminal commands using `argparse`.

This structure keeps the command-line interface, business logic, and file handling separate, making the application easier to understand, test, and maintain.

A more detailed explanation is available in `DESIGN.md`.

## AI Disclosure

AI assistance used during development is documented in `AI_DISCLOSURE.md`.

## Known Limitations

- Only supports EUR; no currency conversion.
- No CSV import or export.
- No option to delete or undo transactions.
- No graphical interface.
- Uses Python floating-point numbers for monetary values.
- Designed for a single local user; simultaneous file writes are not supported.

## Future Improvements

Possible improvements for Release 2 include undo functionality, CSV import and export, monthly reports, and category-based spending summaries.