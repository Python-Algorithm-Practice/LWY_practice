n, m = map(int, input().split())

result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    result = max(min(arr), result)
print(result)