import httpx

from repo_stats.models.repo_model import Repo


def format_table(names: list[str], results: list[Repo | BaseException]) -> str:
    repos = [r for r in results if isinstance(r, Repo)]
    errors = [(n, r) for n, r in zip(names, results) if not isinstance(r, Repo)]

    repos = sorted(
        repos, key=lambda r: r.stargazers_count, reverse=True
    )  # blank 1: sort by what?

    lines = [f"{'repo':<22}{'stars':>10}{'forks':>8}{'open issues':>13}   language"]
    for r in repos:
        lines.append(
            f"{r.full_name:<22}{r.stargazers_count:>10,}"  # blank 2: thousands separator
            f"{r.forks_count:>8,}{r.open_issues_count:>13,}   {r.language or '-'}"
        )
    for name, err in errors:
        if isinstance(err, httpx.HTTPStatusError):
            msg = f"{err.response.status_code} {err.response.reason_phrase}"
        else:
            msg = str(err)
        lines.append(f"{name:<22}ERROR: {msg}")
    return "\n".join(lines)
