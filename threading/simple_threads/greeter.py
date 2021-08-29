import time
import threading

def greeter(name: str, freq: int = 10):
    for n in range(1, freq+1):
        print(f"{n}. Hello {name}!")
        time.sleep(1)


def main():
    # set the target
    t1 = threading.Thread(target=greeter, args=("Adam", 7), daemon=True)

    t2 = threading.Thread(target=greeter, args=("Eve", 5), daemon=True)

    t1.start()
    t2.start()

    print("printing greetings with python threads")
    print(321 * 123)

    t1.join()
    t2.join()
    print("Done")

if __name__ == '__main__':
    main()