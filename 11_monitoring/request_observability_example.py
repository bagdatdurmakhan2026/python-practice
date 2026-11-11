import contextvars
import json
import logging
import time
from collections.abc import Generator
from collections import Counter
from contextlib import contextmanager

_request_id: contextvars.ContextVar[str] = contextvars.ContextVar(
    "request_id",
    default="-",
)
_request_counts: Counter[str] = Counter()


class RequestContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = _request_id.get()
        return True


class JsonLogFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        return json.dumps(
            {
                "level": record.levelname,
                "message": record.getMessage(),
                "request_id": getattr(record, "request_id", "-"),
            }
        )


logger = logging.getLogger("service")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.addFilter(RequestContextFilter())
handler.setFormatter(JsonLogFormatter())
logger.addHandler(handler)
logger.propagate = False


@contextmanager
def observe_request(request_id: str) -> Generator[None, None, None]:
    token = _request_id.set(request_id)
    started = time.perf_counter()
    _request_counts["started"] += 1
    try:
        logger.info("request started")
        yield
    except Exception:
        _request_counts["failed"] += 1
        logger.exception("request failed")
        raise
    else:
        _request_counts["succeeded"] += 1
        logger.info("request completed")
    finally:
        elapsed_ms = (time.perf_counter() - started) * 1000
        logger.info("request duration_ms=%.2f", elapsed_ms)
        _request_id.reset(token)


if __name__ == "__main__":
    with observe_request("req-001"):
        logger.info("processing example operation")
    print(dict(_request_counts))
