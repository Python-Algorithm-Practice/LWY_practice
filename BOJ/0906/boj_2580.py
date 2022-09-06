import sys
input = sys.stdin.readline

s = []
for _ in range(9):
    s.append(list(map(int, input().split())))

zeros = []
for i in range(9):
    for j in range(9):
        if s[i][j] == 0:
            zeros.append([i, j])


def numbers(i, j):
    available = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for k in range(9):
        if s[i][k] in available:
            available.remove(s[i][k])
        if s[k][j] in available:
            available.remove(s[k][j])

    i //= 3
    j //= 3
    for p in range(i * 3, (i + 1) * 3):
        for q in range(j * 3, (j + 1) * 3):
            if s[p][q] in available:
                available.remove(s[p][q])

    return available


can_print = False


def dfs(x):
    global can_print

    if can_print:
        return

    if x == len(zeros):
        for row in s:
            print(*row)
            can_print = True
        return

    else:
        (i, j) = zeros[x]
        available = numbers(i, j)

        for num in available:
            s[i][j] = num
            dfs(x + 1)
            s[i][j] = 0  # 정답 없을 경우 초기화


dfs(0)
