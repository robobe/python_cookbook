import asyncio
import logging
import threading

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

def handler(future: asyncio.Future):
    log.info(future.result())

def executer(loop):
    co = asyncio.run_coroutine_threadsafe(hello("thread"), loop)
    co.add_done_callback(handler)

async def hello(msg):
    log.info(f"start from {msg}")
    await asyncio.sleep(1)
    return f"done {msg}"

loop = asyncio.get_event_loop()
worker = threading.Thread(target=executer, args=(loop,), daemon=True)
worker.start()
t1 = loop.create_task(hello("event loop"))
t1.add_done_callback(handler)
loop.run_forever()