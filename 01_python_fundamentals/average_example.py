def average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Список не должен быть пустым")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print(average([4, 6, 8]))
