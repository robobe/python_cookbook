import asyncio
import logging

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG, datefmt='%H:%M:%S')
log = logging.getLogger(__name__)

def callback(future):
    print(future)

async def main():
    log.info("Hello World")
    task = asyncio.create_task(foo_func("Task"))
    task.add_done_callback(callback)
    await asyncio.sleep(2)
    log.info("end")

async def foo_func(text):
    log.info(text)
    await asyncio.sleep(1)
    return "fone"

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# https://www.youtube.com/watch?v=E7Yn5biBZ58