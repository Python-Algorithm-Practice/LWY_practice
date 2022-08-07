n, m = map(int, input().split());
a, b, d = map(int, input().split())

maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

maps[a][b] = 1
result = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

turn = 0
while True:
    d = (d - 1) % 4
    nx = a + dx[d]
    ny = b + dy[d]
        
    if maps[nx][ny] == 0 and 0 <= nx < n and 0 <= ny < m:
        a = nx
        b = ny
        maps[a][b] = 1
        result += 1
        turn = 0
    else:
        turn += 1
        
    if turn == 4:
        nx = a - dx[d]
        ny = b - dy[d]
        if(maps[nx][ny] == 0):
            a = nx
            b = ny
        else:
            break
        turn = 0

print(result)