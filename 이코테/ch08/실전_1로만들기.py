x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] - 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])

"""
범위 10만 넘어가면 dp또는 이진탐색
탑다운 바텀업
큰 문제 작은 문제로 / 작은 문제가 큰 문제에서도 사용 => 점화식
작은 문제 쪼갠 다음 어떻게 재활용할지 
직접 적어보고 점화식으로
"""