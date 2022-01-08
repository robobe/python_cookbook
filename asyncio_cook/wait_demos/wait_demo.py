import asyncio
from asyncio.tasks import FIRST_COMPLETED
import logging

logging.basicConfig(
    format="[%(levelname)s] %(asctime)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG)
log = logging.getLogger(__name__)

async def do_work(delay, work):
    await asyncio.sleep(delay)
    return work

async def main():
    task1 = asyncio.create_task(do_work(1, "hello1"))
    task2 = asyncio.create_task(do_work(2, "hello2"))
    task3 = asyncio.create_task(do_work(3, "hello3"))
    tasks = {task1, task2, task3}                       # set
    finished, unfinished= await asyncio.wait(tasks,return_when=asyncio.FIRST_COMPLETED)
    # Print result from Task that finish running
    for task in finished:
        log.info(task.result())
    # Cancel unfinished
    for task in unfinished:
        task.cancel()
    await asyncio.wait(unfinished)
asyncio.run(main())
