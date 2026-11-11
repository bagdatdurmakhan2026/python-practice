import os
from dataclasses import dataclass, field
from typing import Mapping


@dataclass(frozen=True)
class AppConfig:
    environment: str
    host: str
    port: int
    debug: bool
    api_token: str = field(repr=False)

    @classmethod
    def from_env(cls, values: Mapping[str, str]) -> "AppConfig":
        environment = values.get("APP_ENV", "development")
        if environment not in {"development", "staging", "production"}:
            raise ValueError("APP_ENV must be development, staging, or production")

        raw_port = values.get("APP_PORT", "8000")
        try:
            port = int(raw_port)
        except ValueError as error:
            raise ValueError("APP_PORT must be an integer") from error
        if not 1 <= port <= 65535:
            raise ValueError("APP_PORT must be between 1 and 65535")

        raw_debug = values.get("APP_DEBUG", "false").lower()
        if raw_debug not in {"true", "false"}:
            raise ValueError("APP_DEBUG must be 'true' or 'false'")

        return cls(
            environment=environment,
            host=values.get("APP_HOST", "127.0.0.1"),
            port=port,
            debug=raw_debug == "true",
            api_token=values.get("APP_API_TOKEN", ""),
        )


if __name__ == "__main__":
    config = AppConfig.from_env(os.environ)
    print(config)
