import asyncio


from repo_stats.github import fetch_all
from repo_stats.table import format_table


async def main() -> None:
    names = ["encode/httpx", "nope/does-not-exist", "astral-sh/uv"]
    results = await fetch_all(names)
    print(format_table(names, results))


asyncio.run(main())
