# System Design

This section practices describing system components and their responsibilities before implementing them.

## Topics

- Identify clients, APIs, services, and data stores
- Trace the flow of a request
- Separate responsibilities and operational concerns

## Example: notes service

[`notes_service_example.md`](notes_service_example.md) sketches a notes API, its service layer, database, and event log.

Use the diagram as a starting point for discussing request flow, validation, persistence, and how failures can be diagnosed.

## Intermediate example: design review

[`notes_service_intermediate_example.md`](notes_service_intermediate_example.md) expands the sketch into requirements, an API outline, a relational data model, failure handling, and scaling trade-offs.

Use the discussion questions at the end to identify missing product requirements before committing to an implementation.
