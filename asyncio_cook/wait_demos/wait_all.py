import asyncio
import logging

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", datefmt="%H:%M:%S",level=logging.DEBUG)
log = logging.getLogger(__name__)

async def foo(n):
    await asyncio.sleep(n)
    log.info(f"Run: {n} sec")


async def main():
    tasks = [foo(1), foo(2), foo(3)]
    await asyncio.gather(*tasks)

asyncio.run(main())