import asyncio

import httpx

from repo_stats.config import Settings
from repo_stats.models.repo_model import Repo

API = "https://api.github.com/repos"


async def fetch_repo(
    client: httpx.AsyncClient, sem: asyncio.Semaphore, name: str
) -> Repo:
    async with sem:
        response = await client.get(f"{API}/{name}")
    response.raise_for_status()
    return Repo.model_validate_json(response.text)


async def fetch_all(names: list[str]) -> list[Repo | BaseException]:
    settings = Settings()
    headers = {}
    if settings.github_token is not None:
        headers["Authorization"] = f"Bearer {settings.github_token.get_secret_value()}"
    sem = asyncio.Semaphore(3)
    async with httpx.AsyncClient() as client:
        tasks = [fetch_repo(client, sem, name) for name in names]
        return await asyncio.gather(*tasks, return_exceptions=True)
