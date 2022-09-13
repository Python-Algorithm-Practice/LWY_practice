import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []


def find_parent(c):
    if parent[c] == c:
        return c
    else:
        parent[c] = find(parent[c])
    return parent[c]


def union(a, b):
    a, b = find_parent(a), find_parent(b)
    parent[max(a, b)] = min(a, b)


def check(a, b):
    return find_parent(a) == find_parent(b)


parent = [i for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])
ts, te = map(int, input().split())

graph.sort(reverse=True)
for i in graph:
    c, a, b = i[0], i[1], i[2]
    c = abs(c)
    union(a, b)
    if check(ts, te):
        print(c)
        break
