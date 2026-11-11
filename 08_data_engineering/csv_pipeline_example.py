import csv
from io import StringIO


def main() -> None:
    data = StringIO("item,amount\nbook,10\npen,3\n")
    rows = csv.DictReader(data)
    total = sum(int(row["amount"]) for row in rows)
    print({"total": total})


if __name__ == "__main__":
    main()
