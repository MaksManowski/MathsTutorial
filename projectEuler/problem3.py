def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution():
    num = 600851475143
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if isPrime(i):
                print(i)
    # check n/i, see if isprime(n/i) returns true. if not repeat.


if __name__ == '__main__':
    solution()