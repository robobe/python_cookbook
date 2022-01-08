import asyncio
import logging

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

async def hello(msg):
    log.info(f"start {msg}")
    await asyncio.sleep(1)
    log.info(f"end {msg}")

loop = asyncio.get_event_loop()
t1 = loop.create_task(hello("hello1"))
t2 = loop.create_task(hello("hello2"))
group = asyncio.gather(t1, t2)
loop.run_until_complete(group)
