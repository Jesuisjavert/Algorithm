import sys
sys.stdin = open('input.txt','r')
dx = [-1,0,1,0] #상우하좌
dy = [0,1,0,-1]

def dfs(x, y):
    stack = []
    cnt = 1
    stack.append([x,y])
    arr[x][y]=0
    while stack:
        x, y = stack.pop(0)
        for direction in range(4):
            movex = x + dx[direction]
            movey = y + dy[direction]
            if 0<= movex <N and 0<=movey<N:
                if arr[movex][movey] == 1:
                    stack.append([movex,movey])
                    arr[movex][movey] = 0
                    cnt +=1
    return cnt
 
N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
# print(*arr)
result = []
for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            result.append(dfs(x,y))
result.sort()
print(len(result))
for a in result:
    print(a)