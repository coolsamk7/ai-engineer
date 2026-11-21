import asyncio
import time


async def fetch(name: str, delay: float) -> str:
    print(f"  start {name}")
    await asyncio.sleep(delay)
    return f"{name} done"


async def main() -> None:
    start = time.perf_counter()
    c = fetch("a", 1)
    print("created")
    print(type(c))
    r1 = await c
    print(r1, f"{time.perf_counter() - start:.1f}s")


asyncio.run(main())


async def blocking_fetch(name: str) -> str:
    time.sleep(1)  # NOT asyncio.sleep
    return f"{name} done"


start = time.perf_counter()
results = await asyncio.gather(blocking_fetch("x"), blocking_fetch("y"))
print(results, f"{time.perf_counter() - start:.1f}s")
