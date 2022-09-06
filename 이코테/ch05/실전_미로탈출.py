"""
5 6
101010
111111
000001
111111
111111
"""
from collections import deque
n, m  = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] == 0):
                continue
            if(arr[nx][ny] == 1):
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

bfs(0, 0)
print(arr[n - 1][m - 1])