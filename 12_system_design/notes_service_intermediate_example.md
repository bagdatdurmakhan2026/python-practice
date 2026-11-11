# Notes service — intermediate design exercise

## Requirements and assumptions

- Users can create, read, update, and delete their own notes.
- A note has an identifier, title, body, owner, and timestamps.
- The initial target is a small single-region service; no specific traffic target is assumed.
- Requests are authenticated before accessing user-owned data.

## Request path

```text
Client
  │ HTTPS + access token
  ▼
Load balancer
  ▼
Stateless Notes API ─────► Authentication provider
  │
  ├──► Relational database
  └──► Structured logs / metrics
```

## API sketch

| Method | Route | Behavior |
| --- | --- | --- |
| `POST` | `/v1/notes` | Validate and create a note for the authenticated user |
| `GET` | `/v1/notes?limit=20&cursor=...` | Return that user's notes in stable order |
| `GET` | `/v1/notes/{id}` | Return one note, without exposing another user's data |
| `PATCH` | `/v1/notes/{id}` | Update supplied fields and refresh `updated_at` |
| `DELETE` | `/v1/notes/{id}` | Delete a note owned by the authenticated user |

Use pagination rather than returning an unbounded collection. Validate request sizes and return consistent client errors for invalid input and missing resources.

## Data model

```text
notes(
  id            UUID primary key,
  owner_id      UUID not null,
  title         VARCHAR(120) not null,
  body          TEXT not null,
  created_at    TIMESTAMP not null,
  updated_at    TIMESTAMP not null
)

Index: (owner_id, updated_at DESC, id)
```

The owner-scoped index supports a user's paginated list. Every read and mutation must include the authenticated `owner_id` in its database predicate.

## Consistency and failure handling

- Commit a note change before returning success.
- Use a transaction for any operation that changes multiple rows.
- Enforce request timeouts and bound page size.
- If the database is unavailable, return a service error and log a request ID; do not report a successful write.
- Make create operations idempotent if clients may retry after a timeout.
- Back up the database and periodically verify that a backup can be restored.

## Scaling and trade-offs

- Keep API instances stateless so they can be replicated behind the load balancer.
- Start with one relational database; add indexes based on observed query patterns.
- Add caching only for measured hot reads, and define invalidation behavior before enabling it.
- Consider read replicas only when read load justifies the added replication lag and operational complexity.
- Store large attachments outside the notes table (for example, object storage) if that requirement is introduced.

## Discussion questions

1. What are the product's availability and recovery-time requirements?
2. How should concurrent edits be detected?
3. What rate limits and data-retention rules are needed?
4. Which metrics would reveal slow queries or rising error rates?
