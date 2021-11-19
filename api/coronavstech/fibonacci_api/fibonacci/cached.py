from functools import lru_cache

cache = {}


def fibonacci_cached(n: int) -> int:
    if n in cache:
        return cache[n]

    if n in [0, 1]:
        return n

    fib_num = fibonacci_cached(n - 1) + fibonacci_cached(n - 2)
    cache[n] = fib_num

    return fib_num


@lru_cache(maxsize=256)
def fibonacci_lru_cached(n: int) -> int:
    if n in [0, 1]:
        return n

    return fibonacci_lru_cached(n - 1) + fibonacci_lru_cached(n - 2)
