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


if __name__ == '__main__':
    for i in range(1,101):
        print(str(i)+":"+str(fib(i)))
