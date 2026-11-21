import asyncio
import time
import httpx


async def get_json(client: httpx.AsyncClient, url: str) -> dict:
    resp = await client.get(url)
    return resp.json()


async def main() -> None:
    async with httpx.AsyncClient(timeout=10) as client:
        start = time.perf_counter()
        data = await get_json(client, "https://httpbin.org/delay/1")
        print(data["url"], f"{time.perf_counter() - start:.1f}s")

        # five calls at once
        start = time.perf_counter()
        urls = [f"https://httpbin.org/delay/1?i={i}" for i in range(5)]
        # results = await asyncio.gather(*(get_json(client, u) for u in urls))
        start = time.perf_counter()
        results = []
        for u in urls:
            results.append(await get_json(client, u))
        print(len(results), f"{time.perf_counter() - start:.1f}s")
        # print(len(results), f"{time.perf_counter() - start:.1f}s")


asyncio.run(main())
