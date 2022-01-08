import asyncio
import logging
from asyncio import Event

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

async def worker(e: Event):
    log.info("start worker")
    await asyncio.sleep(1)
    log.info("end worker")
    e.set()

async def waiter(e: Event):
    await e.wait()
    log.info("start waiter")
    await asyncio.sleep(1)
    log.info("end waiter")

loop = asyncio.get_event_loop()
e = Event()
t1 = loop.create_task(worker(e))
t2 = loop.create_task(waiter(e))
group = asyncio.gather(t1, t2)
loop.run_until_complete(group)
