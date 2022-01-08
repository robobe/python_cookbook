import asyncio
import logging
import threading
import time

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

async def worker():
    counter = 0
    while True:
        log.info(f"done work {counter}")
        counter+=1
        await asyncio.sleep(1)


def thread_work():
    log.info("start thread")
    time.sleep(1)
    log.info("run task")
    asyncio.run_coroutine_threadsafe(worker(), loop)

loop = asyncio.get_event_loop()
t = threading.Thread(target=thread_work, daemon=True)
t.start()
loop.run_forever()

