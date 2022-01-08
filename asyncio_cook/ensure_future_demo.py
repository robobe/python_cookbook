import asyncio
import logging

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

def handler(future):
    print(future.result())

async def hello():
    log.info("hello world")
    await asyncio.sleep(1)
    return True

async def main():
    future = asyncio.ensure_future(hello())
    future.add_done_callback(handler)
    await asyncio.sleep(3)

asyncio.run(main())
