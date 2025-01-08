def solution():
    total = 0
    for i in range(1,1001):
        if i % 3 == 0:
            total = total + i
        if i % 5 == 0:
            total = total + i
        if i % 15 == 0:
            total = total - i
    return total


def solution():
    total = 0
    for i in range(1,1001):
        if i % 3 == 0:
            total = total + i
        elif i % 5 == 0:
            total = total + i
    return total

if __name__ == '__main__':
    print(solution())