import asyncio
import logging

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

async def hello():
    log.info("hello world")

loop = asyncio.get_event_loop()
asyncio.ensure_future(hello())
loop.run_forever()
