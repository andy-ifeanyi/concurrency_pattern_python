import datetime
import random

import colorama

import asyncio

import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

def main():
    limit = 250_000
    print(f"Running standard loop with {limit * 2} actions.")

    t0 = datetime.datetime.now()

    loop = asyncio.get_event_loop()
    data: asyncio.Queue = asyncio.Queue()

    task1 = loop.create_task(generate_data(limit, data))
    task2 = loop.create_task(generate_data(limit, data))
    task3 = loop.create_task(process_data(limit * 2, data))

    final_task = asyncio.gather(task1, task2, task3)

    loop.run_until_complete(final_task)
    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + f"App exiting, total time: {dt.total_seconds():,.2f}", flush=True)



async def generate_data(num: int, data: asyncio.Queue):
    for n in range(1, num + 1):
        await data.put((n * n, datetime.datetime.now()))
        await asyncio.sleep(0)


async def process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        await data.get()
        processed += 1
        await asyncio.sleep(0)


if __name__ == "__main__":
    main()
