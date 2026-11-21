"""Read and write transaction data to a JSON file."""
import json
from pathlib import Path
from .models import Transaction
from .validation import validate_transaction


def load_transactions(path):
    path = Path(path)
    if not path.exists():
        return []
    try:
        records = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(records, list):
        raise ValueError("transaction data must be a JSON list")
    result = []
    seen = set()
    for index, record in enumerate(records, start=1):
        try:
            if not isinstance(record, dict):
                raise ValueError("expected a record object")
            if not isinstance(record.get("id"), str) or not record["id"].startswith("T") or not record["id"][1:].isdigit():
                raise ValueError("invalid transaction id")
            if record["id"] in seen:
                raise ValueError("duplicate transaction id")
            amount = validate_transaction(record["kind"], record["category"], record["amount"], record["date"], record["currency"])
            result.append(Transaction(record["id"], record["date"], record["kind"], record["category"], amount, record["currency"]))
            seen.add(record["id"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"row {index}: {exc}") from exc
    return result


def save_transactions(path, transactions):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps([t.to_dict() for t in transactions], indent=2), encoding="utf-8")
    temporary.replace(path)
