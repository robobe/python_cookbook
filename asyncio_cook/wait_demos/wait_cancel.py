import asyncio


async def task(arg):
    await asyncio.sleep(5)
    return arg


async def cancel_waiting_task(work_task, waiting_task):
    await asyncio.sleep(2)
    waiting_task.cancel()
    try:
        await waiting_task
        print("Waiting done")
    except asyncio.CancelledError:
        print("Waiting task cancelled")

    try:
        res = await work_task
        print(f"Work result: {res}")
    except asyncio.CancelledError:
        print("Work task cancelled")


async def main():
    work_task = asyncio.create_task(task("done"))
    works = {work_task}
    print(type(works))
    waiting = asyncio.create_task(asyncio.wait(works))
    await cancel_waiting_task(work_task, waiting)

    work_task = asyncio.create_task(task("done"))
    waiting = asyncio.gather(work_task)
    await cancel_waiting_task(work_task, waiting)


asyncio.run(main())