import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True)
class Note:
    id: int
    title: str
    body: str


class SqliteNoteRepository:
    def __init__(self, database_path: str = ":memory:") -> None:
        self._connection = sqlite3.connect(database_path)
        self._connection.row_factory = sqlite3.Row
        self._connection.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL CHECK (length(title) > 0),
                body TEXT NOT NULL
            )
            """
        )

    def __enter__(self) -> "SqliteNoteRepository":
        return self

    def __exit__(self, exception_type: object, *_: object) -> None:
        try:
            if exception_type is None:
                self._connection.commit()
            else:
                self._connection.rollback()
        finally:
            self._connection.close()

    def create(self, title: str, body: str) -> Note:
        if not title.strip():
            raise ValueError("title cannot be blank")
        cursor = self._connection.execute(
            "INSERT INTO notes (title, body) VALUES (?, ?)",
            (title.strip(), body),
        )
        note_id = cursor.lastrowid
        if note_id is None:
            raise RuntimeError("SQLite did not return an ID for the inserted note")
        return Note(note_id, title.strip(), body)

    def list_notes(self, *, limit: int = 20, offset: int = 0) -> list[Note]:
        if not 1 <= limit <= 100:
            raise ValueError("limit must be between 1 and 100")
        if offset < 0:
            raise ValueError("offset cannot be negative")
        rows = self._connection.execute(
            """
            SELECT id, title, body FROM notes
            ORDER BY id LIMIT ? OFFSET ?
            """,
            (limit, offset),
        )
        return [Note(row["id"], row["title"], row["body"]) for row in rows]


if __name__ == "__main__":
    with SqliteNoteRepository() as repository:
        repository.create("Architecture", "Keep storage behind a repository.")
        repository.create("Testing", "Use parameterized SQL statements.")
        print(repository.list_notes(limit=1))
