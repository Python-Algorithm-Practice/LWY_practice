n = int(input())
info = []
for _ in range(n):
    info.append(input().split())

info.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(len(info)):
    print(info[i][0])
