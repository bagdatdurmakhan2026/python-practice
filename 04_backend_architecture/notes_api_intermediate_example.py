from itertools import count

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field

app = FastAPI(title="Notes API")
_ids = count(1)
_notes: dict[int, "Note"] = {}


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    body: str = Field(min_length=1, max_length=5000)


class Note(BaseModel):
    id: int
    title: str
    body: str


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/notes", response_model=Note, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate) -> Note:
    note = Note(id=next(_ids), title=payload.title.strip(), body=payload.body)
    if not note.title:
        raise HTTPException(status_code=422, detail="title cannot be blank")
    _notes[note.id] = note
    return note


@app.get("/notes", response_model=list[Note])
def list_notes(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
) -> list[Note]:
    notes = sorted(_notes.values(), key=lambda note: note.id)
    return notes[offset : offset + limit]


@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int) -> Note:
    note = _notes.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="note not found")
    return note
