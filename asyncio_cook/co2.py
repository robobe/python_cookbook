import asyncio
import logging

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

async def do_work(delay, work):
    await asyncio.sleep(delay)
    log.info(work)

async def main():
    log.info("start")
    await do_work(1, "hello")
    await do_work(2, "world")
    log.info("end should take 3 sec")
asyncio.run(main())
