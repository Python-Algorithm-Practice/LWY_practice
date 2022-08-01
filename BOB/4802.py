import queue
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    is_Tree = True
    queue = deque()
    queue.append(x)
    
    while queue:
        now = queue.popleft()
        if visited[now] == 1:   #이미 방문했다면 False
            is_Tree = False
        visited[now] = 1
        for next in tree[now]:
            if visited[next] == 0:
                queue.append(next)
    return is_Tree

count = 0

while True:
    count += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    tree = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    result = 0
    for i in range(1, n + 1):
        if visited[i] == 1:
            continue
        if bfs(i) == True:
            result += 1
    
    if result == 0:
        print("Case {}: No trees.".format(count))
    elif result == 1:
        print("Case {}: There is one tree.".format(count))
    else:
        print("Case {}: A forest of {} trees.".format(count,result))
