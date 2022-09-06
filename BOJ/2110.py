import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()
start = 1
end = house[-1] - house[0]

ans = 0
while(start <= end):
    mid = (start + end) // 2
    cnt = 1
    cur = house[0]

    for i in range(1, n):
        if(cur + mid <= house[i]):
            cur = house[i]
            cnt += 1
    
    if cnt < c:
        end = mid - 1       #거리 좁히기
    else:
        start = mid + 1     #거리 넓히기
        ans = max(ans, mid)

print(ans)
