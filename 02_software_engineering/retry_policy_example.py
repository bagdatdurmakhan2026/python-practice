from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def retry(
    operation: Callable[[], T],
    *,
    attempts: int,
    initial_delay: float,
    retry_on: tuple[type[Exception], ...],
    sleep: Callable[[float], None],
) -> T:
    """Retry selected failures with exponential backoff."""
    if attempts < 1:
        raise ValueError("attempts must be at least one")
    if initial_delay < 0:
        raise ValueError("initial_delay cannot be negative")
    if not retry_on:
        raise ValueError("retry_on must contain at least one exception type")

    for attempt in range(attempts):
        try:
            return operation()
        except retry_on:
            if attempt == attempts - 1:
                raise
            sleep(initial_delay * (2**attempt))

    raise RuntimeError("unreachable")


if __name__ == "__main__":
    failures_remaining = iter((1, 1))

    def flaky_operation() -> str:
        if next(failures_remaining, 0):
            raise ConnectionError("temporary failure")
        return "request succeeded"

    result = retry(
        flaky_operation,
        attempts=3,
        initial_delay=0.25,
        retry_on=(ConnectionError,),
        sleep=lambda delay: print(f"retrying in {delay:.2f}s"),
    )
    print(result)
