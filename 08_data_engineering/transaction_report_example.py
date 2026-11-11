import csv
from collections import defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation
from io import StringIO
from typing import Iterable


def monthly_totals(csv_lines: Iterable[str]) -> dict[tuple[str, str], Decimal]:
    reader = csv.DictReader(csv_lines)
    required = {"date", "category", "amount"}
    if reader.fieldnames is None or not required.issubset(reader.fieldnames):
        raise ValueError(f"CSV must include columns: {', '.join(sorted(required))}")

    totals: defaultdict[tuple[str, str], Decimal] = defaultdict(Decimal)
    for line_number, row in enumerate(reader, start=2):
        try:
            transaction_date = date.fromisoformat(row["date"] or "")
            category = (row["category"] or "").strip()
            amount = Decimal(row["amount"] or "")
        except (ValueError, InvalidOperation) as error:
            raise ValueError(f"invalid transaction on line {line_number}") from error
        if not category:
            raise ValueError(f"empty category on line {line_number}")
        if not amount.is_finite():
            raise ValueError(f"amount must be finite on line {line_number}")
        totals[(transaction_date.strftime("%Y-%m"), category)] += amount
    return dict(totals)


if __name__ == "__main__":
    sample = StringIO(
        "date,category,amount\n"
        "2026-01-03,books,12.50\n"
        "2026-01-15,books,7.50\n"
        "2026-02-02,travel,30.00\n"
    )
    for (month, category), total in sorted(monthly_totals(sample).items()):
        print(f"{month} {category}: {total:.2f}")
