import time
import threading


def greeter(name: str, freq: int = 10):
    for n in range(1, freq + 1):
        print(f"{n}. Hello {name}!")
        time.sleep(1)


def main():
    # set the target
    threads = [
        threading.Thread(target=greeter, args=("Adam", 7), daemon=True),
        threading.Thread(target=greeter, args=("Eve", 5), daemon=True),
        threading.Thread(target=greeter, args=("Abel", 3), daemon=True),
        threading.Thread(target=greeter, args=("Kane", 3), daemon=True),
    ]


    print("starting threads")

    # start the the threads
    [t.start() for t in threads]

    # join / wait on the threads / wait for the completion of the threads
    [t.join() for t in threads]
    print("Done")


if __name__ == "__main__":
    main()
