calculation_fast = 0


def mem_fib():
    cache = {}

    def fast_fib(n):
        global calculation_fast

        calculation_fast += 1

        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fast_fib(n - 2) + fast_fib(n - 1)
                return cache[n]

    return fast_fib


if __name__ == '__main__':
    memoize = mem_fib()
    print(memoize(100))
    print(calculation_fast)
