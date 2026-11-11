import sqlite3


def main() -> None:
    with sqlite3.connect(":memory:") as database:
        database.execute("CREATE TABLE notes (text TEXT)")
        database.execute(
            "INSERT INTO notes (text) VALUES (?)",
            ("Изучить SQLite",),
        )
        notes = database.execute("SELECT text FROM notes").fetchall()
        print(notes)


if __name__ == "__main__":
    main()
