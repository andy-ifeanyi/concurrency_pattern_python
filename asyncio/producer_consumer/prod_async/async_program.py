import datetime
import random

import colorama

import asyncio


def main():
    loop = asyncio.get_event_loop()

    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)

    data: asyncio.Queue = asyncio.Queue()

    task1 = loop.create_task(generate_data(20, data))
    task2 = loop.create_task(generate_data(20, data))
    task3 = loop.create_task(process_data(40, data))

    final_task = asyncio.gather(task1, task2, task3)

    loop.run_until_complete(final_task)
    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + f"App exiting, total time: {dt.total_seconds():,.2f}", flush=True)



async def generate_data(num: int, data: asyncio.Queue):
    for n in range(1, num + 1):
        await data.put((n * n, datetime.datetime.now()))

        print(colorama.Fore.YELLOW + f" -- generated item {n}", flush=True)
        await asyncio.sleep(random.random() + 0.2)


async def process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        item = await data.get()

        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t
        print(
            colorama.Fore.CYAN
            + f" +++ Processed value {value} after {dt.total_seconds():,.2f}",
            flush=True,
        )
        await asyncio.sleep(0.2)


if __name__ == "__main__":
    main()
