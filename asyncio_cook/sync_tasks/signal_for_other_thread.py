import asyncio
import logging
import threading
import time

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)


def worker(event):
    time.sleep(2)
    log.info("Worker finish singal task")
    loop.call_soon_threadsafe(event.set)

async def hello(msg):
    log.info(f"{msg}")
    await event.wait()
    log.info(f"end {msg}")


loop = asyncio.get_event_loop()
event = asyncio.Event()
co = hello("wait to worker")
t = threading.Thread(target=worker, args=(event, ), daemon=True)
t.start()
loop.run_until_complete(co)
