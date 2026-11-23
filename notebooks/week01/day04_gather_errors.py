import asyncio

import httpx


async def get_status(client: httpx.AsyncClient, code: int) -> int:
    resp = await client.get(f"https://httpbin.org/status/{code}")
    resp.raise_for_status()
    return resp.status_code


async def main() -> None:
    codes = [200, 500, 200]
    async with httpx.AsyncClient(timeout=10) as client:
        # A: default gather
        try:
            results = await asyncio.gather(*(get_status(client, c) for c in codes))
            print("A:", results)
        except httpx.HTTPStatusError as e:
            print("A failed:", e.response.status_code)

        # B: return_exceptions=True
        results = await asyncio.gather(
            *(get_status(client, c) for c in codes), return_exceptions=True
        )
        for r in results:
            if isinstance(r, Exception):
                print("B error:", type(r).__name__)
            else:
                print("B ok:", r)


asyncio.run(main())
