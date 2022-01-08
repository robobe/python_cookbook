import asyncio
import logging

WORK_TIME = 2

logging.basicConfig(
    format="[%(levelname)s] %(asctime)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG)
log = logging.getLogger(__name__)

async def sub_work():
    log.info(f"start sub work")
    await asyncio.sleep(2)
    log.info(f"end sub work")

async def do_work(delay: int):
    log.info(f"start main {delay}")
    await sub_work()
    await asyncio.sleep(delay)
    log.info(f"end work {delay}")

async def main():
    task = asyncio.create_task(do_work(WORK_TIME))
    try:
        await asyncio.wait_for(asyncio.shield(task), timeout=1)
        log.info("end success")
    except asyncio.TimeoutError:
        log.error("oops Timeout")

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()