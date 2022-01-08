import asyncio
import logging
from asyncio import Event
import threading
import time

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

def thread_work(e: Event, loop):
    log.info("start thread")
    time.sleep(1)
    log.info("signal task")
    loop.call_soon_threadsafe(e.set)

async def waiter(e: Event):
    log.info("start waiter wait for event")
    await e.wait()
    await asyncio.sleep(1)
    log.info("end waiter")

event_loop = asyncio.get_event_loop()
e = Event()
t1 = event_loop.create_task(waiter(e))
t = threading.Thread(target=thread_work, args=(e, event_loop,), daemon=True)
t.start()
event_loop.run_forever()
