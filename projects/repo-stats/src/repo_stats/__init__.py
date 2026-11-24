import asyncio
import sys

from repo_stats.github import fetch_all
from repo_stats.models.repo_model import Repo
from repo_stats.table import format_table

__all__ = ["Repo", "main"]


def main() -> None:
    names = sys.argv[1:]
    if not names:
        print("usage: repo-stats OWNER/REPO [OWNER/REPO ...]")
        raise SystemExit(1)

    results = asyncio.run(fetch_all(names))
    print(format_table(names, results))

