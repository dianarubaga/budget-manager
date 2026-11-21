
from dataclasses import dataclass, asdict


@dataclass
class Transaction:
    id: str
    date: str
    kind: str
    category: str
    amount: float
    currency: str = "EUR"

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
