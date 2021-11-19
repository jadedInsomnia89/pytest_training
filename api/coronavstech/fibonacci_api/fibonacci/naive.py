def fibonacci_naive(n: int) -> int:
    if n in [0, 1]:
        return n

    return fibonacci_naive(n - 2) + fibonacci_naive(n - 1)
