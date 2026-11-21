import asyncio
import time
import httpx


async def main() -> None:
    sem = asyncio.Semaphore(3)
    start = time.perf_counter()

    async def limited_get(client: httpx.AsyncClient, i: int) -> int:
        async with sem:
            print(f" start {i} at {time.perf_counter() - start:.1f}s ")
            resp = await client.get(f"https://httpbin.org/delay/1?i{i}")
            return resp.status_code

    async with httpx.AsyncClient(timeout=20) as client:
        results = await asyncio.gather(*(limited_get(client, i) for i in range(6)))

    print(results, f"total {time.perf_counter() - start:.1f}s")


asyncio.run(main())
