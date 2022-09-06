import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: continue
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


"""
다익스트라: 시작점에서 다른 모든 최단거리
노드로 넘어감
신장트리 - 사이클 x 크루스칼: 그리디
위상정렬: 큐 구조 방향성에 거스르지 않도록 순서대로
큐가 빌때까지 -> 모든 원소 방문하ㅣㄱ 전에 큐가 비면 사이클

다익스트라 단점: (음일때 사용x)
계속 최솟값 따라가면 음의 사이클에 빠질수도
플로이드 워셜 - 모든 노드들에 시작해서 다른 모든 노드
시간복잡도 단점
"""
