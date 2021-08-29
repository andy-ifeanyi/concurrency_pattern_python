def gen_fib_infinite_sequence():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


if __name__ == '__main__':
    result = gen_fib_infinite_sequence()
    for n in result:
        print(n, end=', ')
        if n > 20000:
            break
