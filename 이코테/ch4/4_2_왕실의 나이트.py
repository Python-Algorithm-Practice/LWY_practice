now = input()
col = int(ord(now[0])) -97
row = int(now[1]) - 1
move = [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
result = 0

for i in range(8):
    nx = col + move[i][0]
    ny = row + move[i][1]
    
    if(nx >= 0 and nx < 8 and ny >= 0 and ny < 8):
        result += 1
    
print(result)