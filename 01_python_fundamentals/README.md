# Python Fundamentals

This section contains Python practice examples, from basic language features to algorithms and data structures.

## Topics

- Functions, variables, collections, and input validation
- Hash tables, sliding windows, and two-pointer techniques
- Working with files and SQLite

## Example: calculating an average

[`average_example.py`](average_example.py) demonstrates a typed function, built-in `sum` and `len`, and explicit handling of an empty list.

Run it from the repository root:

```powershell
python 01_python_fundamentals\average_example.py
```

Expected output: `6.0`.

## Intermediate example: LRU cache

[`lru_cache_example.py`](lru_cache_example.py) implements a generic least-recently-used cache with a fixed capacity. Accessing an item makes it recent; inserting beyond capacity evicts the least recently used item.

```powershell
python 01_python_fundamentals\lru_cache_example.py
```

The output shows the evicted key returning `None`, followed by the cached value `3`.
