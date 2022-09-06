"""
6 4
0100
1110
1000
0000
0111
0000
"""
import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    q = deque()
    q.append([0, 0, 0])
    visit[0][0][0] = 1

    while q:
        a, b, c = q.popleft()

        if a == n - 1 and b == m - 1:
            return visit[a][b][c]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if arr[nx][ny] == 0 and visit[nx][ny][c] == 0:
                visit[nx][ny][c] = visit[a][b][c] + 1
                q.append([nx, ny, c])
            elif arr[nx][ny] == 1 and c == 0:
                visit[nx][ny][c + 1] = visit[a][b][c] + 1
                q.append([nx, ny, c + 1])

    return -1


n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]

print(bfs())
