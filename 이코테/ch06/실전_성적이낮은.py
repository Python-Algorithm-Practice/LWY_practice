import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    data = input().split()
    arr.append((data[0], data[1]))

arr.sort(key = lambda x: x[1])

for i in arr:
    print(i[0], end = ' ')