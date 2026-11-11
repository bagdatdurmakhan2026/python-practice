import logging

logging.basicConfig(level=logging.INFO)


def start_app() -> None:
    logging.info("Приложение запускается")
    logging.info("Статус: running")


if __name__ == "__main__":
    start_app()
