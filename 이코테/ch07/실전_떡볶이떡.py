import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def binary(arr, target, start, end):
    ans = 0
    while start <= end:
        tmp = 0
        mid = (start + end) // 2
        for i in arr:
            if i > mid:
                tmp += i - mid
        if tmp < target:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1

    return ans

print(binary(arr, m, 0, max(arr)))
        