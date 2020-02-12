import sys
sys.stdin = open('input.txt', 'r')
dx = [-1,0,1,1]
dy = [1,1,1,0]
cnt = 1
arr = [list(map(int, input().split())) for _ in range(19)]
answer = [0, 0, 0]
for y in range(19):
    for x in range(19):
        if arr[x][y] != 0:
            color = arr[x][y]
            for move in range(4):
                tx = x + dx[move]
                ty = y + dy[move]
                if 0 <= tx < 19 and 0 <= ty < 19 and arr[tx][ty] == color:
                    if 0 <= x - dx[move] < 19 and 0 <= y - dy[move] < 19:
                        if arr[x - dx[move]][y - dy[move]] == color:
                            continue
                    while 0 <= tx < 19 and 0 <= ty < 19 and arr[tx][ty] == color:
                        cnt += 1
                        tx += dx[move]
                        ty += dy[move]
                    if cnt == 5:
                        answer[0] = color
                        answer[1] = x + 1
                        answer[2] = y + 1
                        break
if answer[0]:
    print(answer[0])
    print(answer[1], answer[2])
else:
    print(answer[0])