from dataclasses import dataclass


@dataclass
class Order:
    price: float
    quantity: int


def calculate_total(order: Order) -> float:
    return order.price * order.quantity


if __name__ == "__main__":
    print(calculate_total(Order(price=10.0, quantity=3)))
