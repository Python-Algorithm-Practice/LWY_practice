n = int(input())
x = list(map(int, input().split()))
count = 0

while True:
    x_max = max(x)
    x.remove(max(x))
    for _ in range(x_max - 1):
        x.remove(min(x))
    count += 1

    if len(x) == 0 or max(x) > len(x):
        break

print(count)
