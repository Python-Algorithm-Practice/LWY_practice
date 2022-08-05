n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
sum = 0

i  = 0
j = 0
while(i < m):
    if j == k:
        sum += arr[1]
        j = 0
    else:
        sum += arr[0]

    i += 1
    j += 1

print(sum)