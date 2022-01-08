import asyncio
import logging

logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
log = logging.getLogger(__name__)

async def hello():
    log.info("hello world")

def main():
    loop = asyncio.get_event_loop()
    loop.create_task(hello())


    loop.run_forever()

main()