import asyncio

import httpx


async def main() -> None:
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get("https://httpbin.org/status/500")
        print("status:", resp.status_code)
        print("got here")
        resp.raise_for_status()
        print("after raise_for_status")


try:
    asyncio.run(main())
except httpx.HTTPStatusError as e:
    print("HTTP error:", e.response.status_code)
