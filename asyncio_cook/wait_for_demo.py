import asyncio
import logging

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

async def do_work(delay, work):
    await asyncio.sleep(delay)
    log.info(work)

async def main():
    log.info("start")
    task = asyncio.create_task(do_work(2, "hello"))
    try:
        await asyncio.wait_for(task, 1)
        log.info("end success")
    except asyncio.TimeoutError:
        log.error("oops Timeout")
    
asyncio.run(main())
