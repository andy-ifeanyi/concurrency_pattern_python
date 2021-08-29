def fibonacci(limit: int) -> list[int]:
    fib_numbers = []

    current, nxt = 0, 1

    while len(fib_numbers) < limit:
        current, nxt = nxt, current + nxt
        fib_numbers.append(current)

    print(fib_numbers)


if __name__ == '__main__':
    fibonacci(20)
