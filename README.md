# Interactive Personal Budget Manager — Release 1

A Python command-line application for recording income and expenses in EUR, listing transactions, and calculating total income, total expenses, and the remaining balance.

## Project Structure

```text
budget-manager/
├── data/
│   └── sample_transactions.csv
├── src/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── models.py
│   ├── services.py
│   ├── storage.py
│   └── validation.py
├── tests/
│   └── test_budget.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
├── README.md
├── DESIGN.md
└── AI_DISCLOSURE.md
```

## Set Up with uv

This project uses `uv` for Python environment and dependency management.

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/dianarubaga/budget-manager.git
cd budget-manager
```

Install and synchronize the project environment:

```bash
uv sync
```

The application modules are located directly inside the `src/` package.

## Run

Display the available commands:

```bash
uv run python -m src --help
```

Add income and expenses:

```bash
uv run python -m src add income 1500 salary --date 2026-11-21
uv run python -m src add expense 20 food --date 2026-11-21
uv run python -m src add expense 50 transport --date 2026-11-21
```

List all transactions:

```bash
uv run python -m src list
```

Generate a financial report:

```bash
uv run python -m src report
```

Expected output when starting with an empty transaction file:

```text
Total income:   1500.00 EUR
Total expenses: 70.00 EUR
Balance:        1430.00 EUR
```

### Use a Different Data File

To use an independent dataset, specify the global `--file` option before the subcommand:

```bash
uv run python -m src --file test_transactions.json add expense 9.5 transport
uv run python -m src --file test_transactions.json report
```

By default, transactions are stored in `transactions.json` in the current working directory. This file is ignored by Git.

### Input Validation

The program accepts the following categories:

- `entertainment`
- `food`
- `housing`
- `other`
- `salary`
- `transport`

All transaction amounts must be positive.

Dates must be valid calendar dates in `YYYY-MM-DD` format.

Transaction types must be either `income` or `expense`.

Invalid inputs are rejected with an error message.

## Test

Run the automated tests using:

```bash
uv run python -m unittest discover -s tests -v
```

The tests cover:

- Normal income, expense, and balance calculations.
- Zero and negative amounts.
- Unknown categories.
- Invalid dates.
- Malformed JSON data.
- Saving and loading transactions.

### Manual Validation Test

Try adding a negative expense:

```bash
uv run python -m src add expense -5 food
```

Expected behavior: the program rejects the amount, displays an error message, and exits with a nonzero status.

## Sample Data

The file `data/sample_transactions.csv` contains three valid and two intentionally invalid records.

These examples demonstrate the expected transaction format and provide boundary cases for testing input validation.

The CSV is included as sample data; CSV import is not implemented in Release 1.

## Design

The application separates responsibilities across different Python modules:

- `models.py`: Defines the transaction data structure.
- `validation.py`: Validates user input and transaction data.
- `services.py`: Handles transactions and budget calculations.
- `storage.py`: Saves and loads transaction data.
- `cli.py`: Processes command-line arguments and displays results.

This separation makes the application easier to maintain, understand, and test.

A more detailed architectural explanation is provided in `DESIGN.md`.

## AI Disclosure

The use of AI assistance during development is documented in `AI_DISCLOSURE.md`.

## Known Limitations

- Supports EUR only; no currency conversion.
- No CSV import or export.
- No undo or delete functionality (undo is an optional stretch challenge).
- Command-line interface only; no graphical dashboard.
- Uses Python `float` values rather than `Decimal`, which may introduce floating-point precision limitations.
- Designed for one local user; simultaneous writes are not supported.

## Future Improvements

Potential improvements for Release 2 include CSV import and export, transaction deletion, undo functionality, category-based budget limits, and monthly spending reports.