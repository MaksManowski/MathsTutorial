def isPalindrome(num: int) -> bool:
    numStr = str(num)
    if numStr[0] == numStr[len(numStr)-1]:
        pass
    # check 1st and last
    # check 2nd and 2nd to last
    return numStr


def solution():
    num = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if isPalindrome(i*j):
                if i*j >= num:
                    num = i*j
    return num


if __name__ == '__main__':
    print(isPalindrome(100))
