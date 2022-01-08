import asyncio
import logging
import random

logging.basicConfig(
    format="[%(levelname)s] %(asctime)s %(message)s", 
    datefmt="%H:%M:%S",
    level=logging.DEBUG)
log = logging.getLogger(__name__)

async def do_work():
    delay = random.randint(1,4)
    log.info(f"start work {delay}")
    await asyncio.sleep(delay)
    log.info(f"end work {delay}")

async def main():
    while True:
        try:
            task = asyncio.create_task(do_work())
            await asyncio.wait_for(task, timeout=2)
            log.info("end success")
            break
        except asyncio.TimeoutError:
            log.error("oops Timeout")

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()