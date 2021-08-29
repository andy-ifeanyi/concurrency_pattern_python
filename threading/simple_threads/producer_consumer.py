import datetime
import random
import time
import threading
import colorama


def generate_data(num: int, data: list):
    for n in range(1, num + 1):
        data.append((n * n, datetime.datetime.now()))
        print(colorama.Fore.YELLOW + f" -- generated item {n}", flush=True)
        time.sleep(random.random() + 0.2)


def process_data(num, data):
    processed = 0
    while processed < num:
        item = data.pop(0)
        if not item:
            time.sleep(0.01)
            continue

        processed += 1
        value = item[0]
        tt = item[1]
        dt = datetime.datetime.now() - tt

        print(
            colorama.Fore.CYAN
            + f" +++ Processed value {value} after {dt.total_seconds():,.2f}",
            flush=True,
        )
        time.sleep(0.2)


def main():
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)
    data = []
    # set the target
    threads = [
        threading.Thread(target=generate_data, args=(20, data), daemon=True),
        threading.Thread(target=generate_data, args=(20, data), daemon=True),
        threading.Thread(target=process_data, args=(40, data), daemon=True),
    ]

    print("starting threads")

    # start the the threads
    [t.start() for t in threads]

    # join / wait on the threads / wait for the completion of the threads
    [t.join() for t in threads]
    print("Done")
    dt = datetime.datetime.now() - t0
    print(
        colorama.Fore.WHITE + f"App exiting, total time: {dt.total_seconds():,.2f}",
        flush=True,
    )


if __name__ == "__main__":
    main()
