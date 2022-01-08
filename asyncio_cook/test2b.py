import asyncio
import logging
import threading
import time

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

lock_ = asyncio.Lock()

class Worker():
    def __init__(self) -> None:
        self.__event = asyncio.Event()
        self.__w = threading.Thread(target=self.worker, daemon=True)
        

    def worker(self):
        time.sleep(2)
        loop.call_soon_threadsafe(self.__event.set)

    async def hello(self, msg):
        async with lock_:
            self.__w.start()
            log.info(f"{msg} from id: {id(self)}")
            await self.__event.wait()
            log.info(f"end {msg}")

async def runner(name):
    w = Worker()
    asyncio.ensure_future(w.hello(name))

loop = asyncio.get_event_loop()

loop.create_task(runner("task1"))
loop.create_task(runner("task2"))
loop.run_forever()
