from collections import OrderedDict
from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class LRUCache(Generic[K, V]):
    """A small least-recently-used cache with a fixed maximum size."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be greater than zero")
        self._capacity = capacity
        self._items: OrderedDict[K, V] = OrderedDict()

    def get(self, key: K) -> V | None:
        if key not in self._items:
            return None
        self._items.move_to_end(key)
        return self._items[key]

    def put(self, key: K, value: V) -> None:
        self._items[key] = value
        self._items.move_to_end(key)
        if len(self._items) > self._capacity:
            self._items.popitem(last=False)

    def __len__(self) -> int:
        return len(self._items)


if __name__ == "__main__":
    cache: LRUCache[str, int] = LRUCache(capacity=2)
    cache.put("python", 3)
    cache.put("sql", 2)
    cache.get("python")
    cache.put("docker", 1)

    print(cache.get("sql"))  # None: "sql" was least recently used.
    print(cache.get("python"))
