# Databases

This section practices relational database fundamentals with Python's built-in SQLite support.

## Topics

- Create tables and insert records
- Use parameterized SQL statements
- Query and fetch stored data

## Example: an in-memory notes table

[`sqlite_example.py`](sqlite_example.py) creates a temporary SQLite database, inserts a note using a parameterized query, and reads it back.

Run from the repository root:

```powershell
python 07_databases\sqlite_example.py
```

The database exists only in memory and is discarded when the script exits.
