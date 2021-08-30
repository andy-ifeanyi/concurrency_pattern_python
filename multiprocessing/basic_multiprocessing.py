import multiprocessing
import math
import logging
import datetime
from multiprocessing.pool import Pool

logging.basicConfig(
    format="%(asctime)s - %(name)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %I:%M:%S %p",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def sqrt_even_numbers(limit: int):
    for n in range(1, limit + 1):
        if n % 2 == 0:
            # math.sqrt(n)
            # print(f"number: {n}, square root: {math.sqrt(n)}")
            logger.info("number: %s, square root: %s", n, math.sqrt(n))


def main():
    # sqrt_even_numbers(10)
    print("Starting multiprocessing now...")

    t0 = datetime.datetime.now()
    # create pool of processors to use
    pool = Pool(processes=multiprocessing.cpu_count())

    # send computation task to different processors in the pool
    pool.apply_async(func=sqrt_even_numbers, args=(100000,))
    pool.apply_async(func=sqrt_even_numbers, args=(200000,))
    pool.apply_async(func=sqrt_even_numbers, args=(300000,))
    pool.apply_async(func=sqrt_even_numbers, args=(400000,))

    pool.close()
    pool.join()

    dt = datetime.datetime.now() - t0

    print(f"Total time taken in seconds: {dt.total_seconds():,.2f}")


if __name__ == "__main__":
    # sqrt_even_numbers()
    main()
