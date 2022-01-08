import asyncio
import logging
from asyncio import Event
import threading
import time

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

def thread_work(e: Event, loop):
    log.info("start thread")
    for i in range(3):
        time.sleep(2)
        log.info("signal task")
        loop.call_soon_threadsafe(e.set)

async def waiter():
    log.info("start waiter wait for event")
    await e.wait()
    e.clear()
    await asyncio.sleep(0.5)
    log.info("end waiter")

async def worker():
    while True:
        await asyncio.wait_for(waiter(), timeout=3)
        log.info("done")
        break

event_loop = asyncio.get_event_loop()
e = Event()
t1 = event_loop.create_task(worker())
t = threading.Thread(target=thread_work, args=(e, event_loop,), daemon=True)
t.start()
event_loop.run_forever()
