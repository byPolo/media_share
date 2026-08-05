# media-share

A small media sharing platform — upload images and videos, give them a caption, and browse
what has been posted.

The real purpose of this project is **learning FastAPI**. It is a practice codebase rather than
a product, so the feature set is deliberately small and the code favours being readable and
easy to reason about over being clever or complete.

## Scope

A deliberately simple set of features:

- Create a post with a media file and a caption
- List all posts, and fetch a single post by id
- Store media in an external service (ImageKit) and keep the metadata in the database
- User accounts and authentication

The frontend will be built with **Streamlit** — a thin UI over the API, chosen so the focus
stays on the backend.

## Stack

| Piece | Choice |
|---|---|
| API | FastAPI |
| Server | Uvicorn |
| Database | SQLite via SQLAlchemy (async, `aiosqlite`) |
| Media storage | ImageKit |
| Auth | fastapi-users |
| Frontend | Streamlit |
| Packaging | uv, Python 3.14 |

SQLite is a local development choice. Because everything goes through SQLAlchemy, swapping in
another database means changing `DATABASE_URL` in [app/db.py](app/db.py) rather than rewriting
queries.

## Running it

```bash
uv sync
uv run main.py
```

The API starts on <http://localhost:8000>, with interactive docs at
<http://localhost:8000/docs>.

## Layout

```
main.py           # entry point, starts uvicorn
app/
  app.py          # FastAPI app and routes
  db.py           # SQLAlchemy models, engine, session
  schemas.py      # pydantic request/response models
```

## Status

Early. The post endpoints currently read and write an in-memory dictionary while the routes and
request shapes are worked out; the SQLAlchemy `Post` model and its tables exist and are created
on startup, but the endpoints are not wired to them yet. Media upload, auth, and the Streamlit
frontend are still to come.
