import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())


def is_prime(a):
    if a == 1:
        return False

    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return False
    return True


def make(num):
    if num >= 10 ** (n - 1):
        print(num)
    else:
        for i in range(10):
            now = num * 10 + i
            if is_prime(now):
                make(now)


make(2)
make(3)
make(5)
make(7)
