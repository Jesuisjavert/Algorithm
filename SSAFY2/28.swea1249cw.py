from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append((0,0)) 
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny <N:
                if distance[nx][ny] > distance[x][y] + int(arr[x][y]):
                    distance[nx][ny] = distance[x][y] + int(arr[x][y])
                    q.append((nx,ny))
T = int(input())
 
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    distance = [[1000000] * N for _ in range(N)]
    distance[0][0] = 0
    bfs()
    print('#{} {}'.format(tc,distance[N-1][N-1]))