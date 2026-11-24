# repo-stats

Compare GitHub repositories from the command line. Fetches repos **concurrently**
from the GitHub API, validates responses with **Pydantic**, and prints a table
sorted by stars. A repo that fails (e.g. 404) shows as an `ERROR` row instead of
crashing the run.

## Run

```bash
uv run repo-stats pydantic/pydantic encode/httpx astral-sh/uv nope/does-not-exist
```

```
repo                       stars   forks  open issues   language
astral-sh/uv              92,580   3,928        3,107   Rust
pydantic/pydantic         29,641   3,265          647   Python
encode/httpx              15,848   2,019          156   Python
nope/does-not-exist   ERROR: 404 Not Found
```

## GitHub token (optional)

Without a token GitHub allows 60 requests/hour. To raise the limit, copy
`.env.example` to `.env` and set `GITHUB_TOKEN`. It is read via
pydantic-settings as a `SecretStr` and sent as a `Bearer` header.

## How it works

- `models/repo_model.py` – `Repo` Pydantic model (only the 5 fields we need)
- `github.py` – one shared `httpx.AsyncClient`, max 3 requests at a time
  (`asyncio.Semaphore`), `gather(return_exceptions=True)` for partial failures
- `table.py` – pure formatting function (sort + f-string table)

## Develop

```bash
uv run pytest
uv run ruff check . && uv run ruff format --check .
uv run mypy src
```
