import asyncio
import logging
import threading
import time

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

event = asyncio.Event()

def worker():
    time.sleep(2)
    loop.call_soon_threadsafe(event.set)

async def hello(msg):
    log.info(msg)
    await event.wait()
    log.info(f"end {msg}")

loop = asyncio.get_event_loop()
loop.create_task(hello("Task"))
t = threading.Thread(target=worker, daemon=True)
t.start()
loop.run_forever()
