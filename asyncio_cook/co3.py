import asyncio
import logging

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

async def do_work(delay, work):
    await asyncio.sleep(delay)
    log.info(work)

async def main():
    log.info("start")
    t1 = asyncio.create_task(do_work(1, "hello"))
    t2 = asyncio.create_task(do_work(2, "world"))
    await t1
    await t2
    log.info("end should take 2 sec")
asyncio.run(main())
