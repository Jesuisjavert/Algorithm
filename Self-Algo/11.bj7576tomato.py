import sys
sys.stdin = open('input.txt','r')
dx = [-1,0,1,0] #상우하좌
dy = [0,1,0,-1]
def tomato(x,y):
    stack = []
    cnt = 1
    stack.append([x,y])
    while stack:
        x, y = stack.pop(0)
        for direction in range(4):
            movex = x + dx[direction]
            movey = y + dy[direction]
            if 0<=movex<M and 0<=movey<N:
                if arr[movex][movey] == 0:
                    stack.append([movex,movey])
                    arr[movex][movey]=1
        cnt+=1
    return cnt

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]
visit = []
cnt = 0
for x in range(M):
    for y in range(N):
        if arr[x][y] == 1:
            cnt = tomato(x,y)
print(cnt)

# for x in range(M):
#     for y in range(N):
#         if arr[x][y]==0:
#             cnt = -1 다 돈 시점에서 아직 안 익은게 남아 있으면 -1로 판별되도록

