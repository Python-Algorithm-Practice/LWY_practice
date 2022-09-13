import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))


def boundary(x, y, d1, d2):
    people = [0, 0, 0, 0, 0]
    temp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(d1 + 1):
        temp[x + i][y - i] = 5
        temp[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        temp[x + i][y + i] = 5
        temp[x + d1 + i][y - d1 + i] = 5

    # 경계선 만나면 안은 5번 선거구
    for i in range(x + 1, x + d1 + d2):
        flag = False
        for j in range(1, n + 1):
            if temp[i][j] == 5:
                flag = not flag
            if flag:
                temp[i][j] = 5

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 1번
            if i < x + d1 and j <= y and temp[i][j] == 0:
                people[0] += arr[i][j]
            # 2번
            elif i <= x + d2 and y < j and temp[i][j] == 0:
                people[1] += arr[i][j]
            # 3번
            elif x + d1 <= i and j < y - d1 + d2 and temp[i][j] == 0:
                people[2] += arr[i][j]
            # 4번
            elif x + d2 < i and y - d1 + d2 <= j and temp[i][j] == 0:
                people[3] += arr[i][j]
            # 5번
            elif temp[i][j] == 5:
                people[4] += arr[i][j]

    return max(people) - min(people)


ans = 1e9
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    ans = min(ans, boundary(x, y, d1, d2))

print(ans)
