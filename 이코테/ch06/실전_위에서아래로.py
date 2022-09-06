import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(3):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(3):
    print(arr[i], end = ' ')