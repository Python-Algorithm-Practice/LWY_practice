import sys
import heapq
input = sys.stdin.readline

n = int(input())
card = []
answer = 0

for _ in range(n):
    heapq.heappush(card, int(input()))

while(len(card) > 1):
    c1 = heapq.heappop(card)
    c2 = heapq.heappop(card)
    answer += (c1 + c2)
    heapq.heappush(card, c1+ c2)
  
print(answer)