import asyncio
import logging

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

async def do_work(delay, work):
    await asyncio.sleep(delay)
    log.info(work)

async def main():
    co = do_work(1, "hello coroutine")
    log.info(type(co))
    await co
    
asyncio.run(main())
