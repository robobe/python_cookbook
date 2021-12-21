import asyncio
import logging

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG, datefmt='%H:%M:%S')
log = logging.getLogger(__name__)

async def main():
    log.info("Hello World")
    task = asyncio.create_task(foo_func("Task"))
    await asyncio.sleep(2)
    log.info("end")

async def foo_func(text):
    log.info(text)
    await asyncio.sleep(1)

asyncio.run(main())


# https://www.youtube.com/watch?v=E7Yn5biBZ58