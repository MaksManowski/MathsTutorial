def fib(n):
    if n < 2:
        return 1
    n_1 = 1
    n_2 = 1
    while n > 2:
        new_n = n_1 + n_2
        n_2 = n_1
        n_1 = new_n
        n = n - 1
    return n_1


def solution():
    total = 0
    n = 1
    while fib(n) < 4_000_000:
        if fib(n) % 2 == 0:
            total = total + fib(n)
        n = n + 1
    return total

if __name__ == '__main__':
    print(solution())