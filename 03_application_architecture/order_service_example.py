from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class OrderRequest:
    item: str
    quantity: int


@dataclass(frozen=True)
class Order:
    order_id: int
    item: str
    quantity: int
    total: int


class OrderRepository(Protocol):
    def save(self, order: Order) -> Order:
        ...


class InMemoryOrderRepository:
    def __init__(self) -> None:
        self._orders: list[Order] = []

    def save(self, order: Order) -> Order:
        saved = Order(
            order_id=len(self._orders) + 1,
            item=order.item,
            quantity=order.quantity,
            total=order.total,
        )
        self._orders.append(saved)
        return saved


class OrderService:
    def __init__(
        self,
        repository: OrderRepository,
        prices: dict[str, int],
        inventory: dict[str, int],
    ) -> None:
        self._repository = repository
        self._prices = prices
        self._inventory = inventory

    def place_order(self, request: OrderRequest) -> Order:
        if request.quantity <= 0:
            raise ValueError("quantity must be greater than zero")
        if request.item not in self._prices:
            raise ValueError(f"unknown item: {request.item}")
        if request.quantity > self._inventory.get(request.item, 0):
            raise ValueError(f"not enough inventory for {request.item}")

        order = Order(
            order_id=0,
            item=request.item,
            quantity=request.quantity,
            total=self._prices[request.item] * request.quantity,
        )
        saved_order = self._repository.save(order)
        self._inventory[request.item] -= request.quantity
        return saved_order


if __name__ == "__main__":
    repository = InMemoryOrderRepository()
    service = OrderService(
        repository=repository,
        prices={"book": 12},
        inventory={"book": 5},
    )
    print(service.place_order(OrderRequest(item="book", quantity=2)))
