import asyncio
import logging

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

async def hello():
    log.info("hello world")

co = hello()
print(co)
asyncio.run(co)
