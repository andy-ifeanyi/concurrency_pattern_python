import datetime
import math
import multiprocessing


def main():
    do_computation(1)

    t0 = datetime.datetime.now()

    print(f"Doing math on {multiprocessing.cpu_count():,} processors.")

    processor_count = multiprocessing.cpu_count()

    pool = multiprocessing.Pool()

    for n in range(1, processor_count + 1):
        pool.apply_async(
            do_computation,
            (30_000_000 * (n - 1) / processor_count, 30_000_000 * n / processor_count),
        )

    pool.close()
    pool.join()

    dt = datetime.datetime.now() - t0
    print(f"Time taken in seconds: {dt.total_seconds():,.2f}")


def do_computation(start=0, num=10):
    pos = start

    k_sq = 1000 * 1000

    while pos < num:
        pos += 1
        math.sqrt((pos - k_sq) * (pos - k_sq))


if __name__ == "__main__":
    main()
