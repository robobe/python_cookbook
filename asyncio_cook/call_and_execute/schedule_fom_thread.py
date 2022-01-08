import asyncio
import logging
import threading
import time
from functools import partial

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

def foo(method):
    log.info(f"running foo using {method}")

def executer(loop: asyncio.BaseEventLoop):
    time.sleep(1)
    loop.call_soon_threadsafe(foo, "direct")
    func = partial(foo, "partial")
    loop.call_soon_threadsafe(func)

loop = asyncio.get_event_loop()
worker = threading.Thread(target=executer, args=(loop,), daemon=True)
worker.start()
loop.run_forever()